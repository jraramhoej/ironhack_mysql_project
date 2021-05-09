import mysql.connector

def sql_action(query):

    # establish connection to a database
    connection = mysql.connector.connect(user='root', password='18Rj7192!', host='localhost', database='sakila',
                                         auth_plugin='mysql_native_password')

    # try / except (or if statement) to check if connected
    if connection.is_connected():
        print("Connection open.")
    else:
        print("Connection is not successfully open.")

    # define object used to interact with the database
    cursor = connection.cursor()

    # execute query, call cursor to execute
    cursor.execute(query)
    print("Query executed.")

    # commit changes to MySQL
    connection.commit()
    print("Committed to MySQL.")

    # clear the cursor
    cursor.close()
    connection.close()



