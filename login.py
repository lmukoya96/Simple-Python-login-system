import mysql.connector
from personal_info import get_personal_info
from personal_info import store_personal_info
from software import welcome_to_software

def existing_user():
    # Establish a connection
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="your_password",
        database="simple_softwaredb"
    )

    # Create a cursor
    cursor = cnx.cursor()

    # Get login credentials
    username = input("Username: ")
    password = input("Password: ")

    # Execute SQL query
    query = "SELECT * FROM personal_info WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    # Fetch the result
    result = cursor.fetchone()

    if result:
        print("Welcome back, " + username)

        #User is able to access software
        welcome_to_software()
    else:
        print("Invalid username or password")
        #User is sent back to the login page
        existing_user()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

def new_user():
    # Get personal information from the user
    info = get_personal_info()

    # Store personal information in the database
    store_personal_info(info)

    #New user will now be promted to login
    existing_user()

def main():
    #Identify is user is new or existing
    user_info = input("New or existing user(new/existing): ")
    if user_info.lower() == "new":
        new_user()
    elif user_info.lower() == "existing":
        existing_user()
    else:
        print("Invalid input...")


if __name__ == "__main__":
    main()