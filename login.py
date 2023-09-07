import mysql.connector
from personal_info import User
from software import welcome_to_software

class Login:
    def existing_user():
        # Establish a connection
        cnx = mysql.connector.connect(
            host="your_connection",
            user="your_username",
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
            print("Welcome, " + username)

            #User is able to access software
            welcome_to_software()
        else:
            print("Invalid username or password")
            #User is sent back to the login page
            Login.existing_user()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

    def new_user():
        # Get personal information from the user
        info = User.get_personal_info()

        # Store personal information in the database
        User.store_personal_info(info)

        #New user will now be promted to login
        Login.existing_user()

def main():
    #Identify is user is new or existing
    user_info = input("New or existing user(new/existing): ")
    if user_info.lower() == "new":
        Login.new_user()
    elif user_info.lower() == "existing":
        Login.existing_user()
    else:
        print("Invalid input...")


if __name__ == "__main__":
    main()