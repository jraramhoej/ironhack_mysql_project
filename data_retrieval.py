from switchup_schools import schools
import re
import pandas as pd
import requests
from datetime import datetime
import numpy as np
from nltk.corpus import stopwords
stop = stopwords.words('english')

# define subset of schools
schools = {
    'ironhack': schools["ironhack"],
    'app-academy': schools["app-academy"],
    'springboard': schools["springboard"]
}

def get_comments_school(school):

    TAG_RE = re.compile(r'<[^>]+>')

    # defines url to make api call to data -> dynamic with school if you want to scrape competition
    url = "https://www.switchup.org/chimera/v1/school-review-list?mainTemplate=school-review-list&path=%2Fbootcamps%2F" + school + "&isDataTarget=false&page=3&perPage=10000&simpleHtml=true&truncationLength=250"

    # makes get request and converts answer to json
    # url defines the page of all the information, request is made, and information is returned to data variable
    data = requests.get(url).json()

    # converts json to dataframe
    reviews = pd.DataFrame(data['content']['reviews'])

    # aux function to apply regex and remove tags
    def remove_tags(x):
        return TAG_RE.sub('', x)

    reviews['review_body'] = reviews['body'].apply(remove_tags)
    reviews['school'] = school
    return reviews

def generate_school_dfs():

    # get the reviews for each school
    reviews = pd.concat([get_comments_school(school) for school in schools.keys()])

    # replace NaN with None
    reviews = reviews.replace(np.nan, None, regex=True)

    # Change datetime format of createdAt column to YYYY-MM-DD
    reviews["createdAt"] = pd.to_datetime(reviews["createdAt"]).dt.strftime('%Y-%m-%d')

    # Change graduatingYear column to display year YYYY instead of float
    reviews["graduatingYear"] = pd.to_datetime(reviews["graduatingYear"], format="%Y").dt.strftime('%Y')

    # create new column with whole years between graduation and review
    def years_since_graduation(row):
        return datetime.strptime(row["createdAt"], "%Y-%m-%d") - datetime.strptime(row["graduatingYear"], "%Y")

    reviews["years_since_graduation"] = (reviews.apply(years_since_graduation, axis=1) / np.timedelta64(1, 'Y')).astype(int)

    # clean review_body, name and tagline from double quotation marks
    def clean_quotes(x):
        return x.replace("\"", "")

    reviews["review_body"] = reviews["review_body"].apply(clean_quotes)
    reviews["name"] = reviews["name"].apply(clean_quotes)
    reviews["tagline"] = reviews["tagline"].apply(clean_quotes)

    # Remove punctuation and special characters in review_body
    reviews["review_body"] = reviews["review_body"].replace("[.!?\\-:,;/]", "", regex=True)

    # create words dataframe

    # function to split review_body and create dicts with wordlists and review_id
    def split_text(row):
        return {"word": [word.lower() for word in row["review_body"].split() if word.lower() not in stop], "review_id": row["id"]}

    # apply split_texts to the dataframe
    words = reviews.apply(split_text, axis=1)

    # Create new data frame
    words = pd.DataFrame(list(words))

    # explode lists into new rows
    words = words['word'].apply(lambda x: pd.Series(x)).stack().reset_index(level=1, drop=True).to_frame('word').join(words[['review_id']], how='left')

    return {"reviews": reviews, "words": words}

