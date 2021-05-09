# files and libraries
import create_mysql_database
import data_retrieval
import database_queries


if __name__ == '__main__':

    # dataframes
    reviews = data_retrieval.generate_school_dfs()["reviews"]
    words = data_retrieval.generate_school_dfs()["words"]

    # create database
    create_mysql_database.sql_action(database_queries.create_database)

    # create tables
    create_mysql_database.sql_action(database_queries.create_reviews)
    create_mysql_database.sql_action(database_queries.create_students)
    create_mysql_database.sql_action(database_queries.create_words)

    # populate tables

    # reviews
    for review_id, tagline, created_at, years_since_graduation, overall_score, overall, curriculum, job_support, review_body, school in zip(reviews["id"], reviews["tagline"], reviews["createdAt"], reviews["years_since_graduation"], reviews["overallScore"], reviews["overall"], reviews["curriculum"], reviews["jobSupport"], reviews["review_body"], reviews["school"]):

        # define query
        query = "INSERT INTO switchup.reviews(review_id, tagline, created_at, years_since_graduation,overall_score, overall, curriculum, job_support, review_body, school_name) VALUES(" + \
        str(review_id) + ", \"" + \
        str(tagline) + "\", " + \
        "STR_TO_DATE(\"" + str(created_at) + "\", \"%Y-%m-%d\"), " + \
        str(years_since_graduation) + ", " + \
        str(overall_score) + ", " + \
        str(overall) + ", " + \
        str(curriculum) + ", " + \
        str(job_support) + ", \"" + \
        str(review_body) + "\", \"" + \
        str(school) + "\");"

        # execute query
        create_mysql_database.sql_action(query)

    # students
    for review_id, name, graduating_year, is_alumni, job_title, program, school in zip(reviews["id"], reviews["name"], reviews["graduatingYear"], reviews["isAlumni"], reviews["jobTitle"], reviews["program"], reviews["school"]):

        # define query
        query = "INSERT INTO switchup.students(review_id, student_name, graduating_year, is_alumni, job_title, program, school_name) VALUES(" + \
        str(review_id) + ", \"" + \
        str(name) + "\", " + \
        str(graduating_year) + ", " + \
        str(is_alumni) + ", \"" + \
        str(job_title) + "\", \"" + \
        str(program) + "\", \"" + \
        str(school) + "\");"

        # execute query
        create_mysql_database.sql_action(query)

    # words
    for word, review_id in zip(words["word"], words["review_id"]):

        # define query
        query = "INSERT INTO switchup.words(word, review_id) VALUES(\"" + \
        str(word) + "\", " + \
        str(review_id) + ");"

        # execute query
        create_mysql_database.sql_action(query)
