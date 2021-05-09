import requests
from bs4 import BeautifulSoup

def get_bootcamps():
    # Empty lists for storing schools
    list_of_bootcamps = []

    index = 0

    # run through the 88 pages of schools
    for x in range(0, 88):

        # specify url for each page
        index = index + 1
        page_number = index
        url = 'https://www.switchup.org/coding-bootcamps-reviews/?page=' + str(page_number)

        # Request
        r1 = requests.get(url)

        # We'll save in coverpage the cover page content
        coverpage = r1.content

        # Soup creation
        soup1 = BeautifulSoup(coverpage, 'html.parser')

        # find schools
        school_page = soup1.find_all('a', class_='bootcamp-list__row--review-count')

        # Loop through the 10 links
        for n in range(0, 10):

            # Getting the link of the article
            start = 'https://www.switchup.org'
            end = school_page[n]["href"].replace("?src=list-featured", "")
            link = start + end

            # get the name of the school from the link
            bootcamp_name = str(link).replace("https://www.switchup.org/bootcamps/", "")

            # Reading the content (it is divided in paragraphs)
            page = requests.get(link)
            page_content = page.content
            soup_page = BeautifulSoup(page_content, 'html.parser')

            # retrieve school id
            bootcamp_id = soup_page.find('page-data')['bootcamp-id']

            # retrieve school id
            list_of_bootcamps.append({bootcamp_name: int(bootcamp_id)})

    list_of_bootcamps = {k: v for d in list_of_bootcamps for k, v in d.items()}

    return list_of_bootcamps

