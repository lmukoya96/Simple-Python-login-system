import mysql.connector
from personal_info import User
from software import welcome_to_software

class Login:
    @staticmethod
    def existing_user():
        # Establish a connection
        cnx = User.Server_Connection()

        # Create a cursor
        cursor = cnx.cursor()

        # Get login credentials
        username = input("Username: ")
        password = input("Password: ")

        # Execute SQL query to compare given username and password.
        query = "SELECT * FROM personal_info WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print("Welcome, " + username)

            # Execute SQL query to set the user as logged in.
            update_query = "UPDATE personal_info SET logged_in = 1 WHERE username = %s"
            cursor.execute(update_query, (username,))
            cnx.commit()

            print("You are now logged in.")

            #User is able to access software
            welcome_to_software()
        else:
            print("Invalid username or password")
            #User is sent back to the login page
            Login.existing_user()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

    @staticmethod
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