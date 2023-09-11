import mysql.connector
from mysql.connector import errorcode

class User:
    def get_personal_info():
        # Prompt user for personal information
        first_name = input("Enter your First Name: ")
        last_name = input("Enter your Last Name: ")
        date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
        phone_number = input("Enter your Phone Number: ")
        country = input("Enter your Country: ")
        street = input("Enter your Street: ")
        city = input("Enter your City: ")
        state = input("Enter your State: ")
        email = input("Enter your Email: ")
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        logged_in = 0
        
        # Return personal information as a dictionary
        personal_info = {
            "First Name": first_name,
            "Last Name": last_name,
            "Date of Birth": date_of_birth,
            "Phone Number": phone_number,
            "Country": country,
            "Street": street,
            "City": city,
            "State": state,
            "Email": email,
            "Username": username,
            "Password": password,
            "logged_in": logged_in
        }
        
        return personal_info
    
    # Connect to the MySQL server.
    def Server_Connection():
        cnx = mysql.connector.connect(
            host="your_connection",
            user="your_username",
            password="your_password",
            database="simple_softwaredb"
        )
        return cnx
    
    def store_personal_info(personal_info):
        try:
            User.Server_Connection()

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                # The database does not exist, so create it.
                cnx = mysql.connector.connect(
                    host="your_connection",
                    user="your_username",
                    password="your_password",
                )
                cursor = cnx.cursor()

                # Create the database
                cursor.execute("CREATE DATABASE simple_softwaredb")
                cursor.execute("USE simple_softwaredb")
                cursor.execute("CREATE TABLE personal_info (user_id INT PRIMARY KEY AUTO_INCREMENT, first_name TEXT(255), last_name TEXT(255), date_of_birth DATE, phone_number VARCHAR(15) UNIQUE, country TEXT(255), street TEXT(255), city TEXT(255), state TEXT(255), email VARCHAR (50) UNIQUE, username TEXT(255), password TEXT(255), logged_in BOOL)")
                cursor.execute("ALTER TABLE personal_info AUTO_INCREMENT = 10001")       
                cnx.database = "simple_softwaredb"

            else:
                print("Error connecting to MySQL server:", error)
                return

        finally:
            if 'cursor' in locals():
                cursor.close()

        try:
            User.Server_Connection()

            # Create a cursor object to interact with the database
            cursor = cnx.cursor()

            # Define the SQL query
            query = """
            INSERT INTO personal_info (first_name, last_name, date_of_birth, phone_number, country, street, city, state, email, username, password, logged_in)
            VALUES (%(First Name)s, %(Last Name)s, %(Date of Birth)s, %(Phone Number)s, %(Country)s, %(Street)s, %(City)s, %(State)s, %(Email)s, %(Username)s, %(Password)s, %(logged_in)s)
            """

            # Execute the query
            cursor.execute(query, personal_info)

            # Commit the changes to the database
            cnx.commit()
            print("Personal information stored successfully!")

        except mysql.connector.Error as error:
            print("Error storing personal information:", error)

        # Close the cursor and connection
        cursor.close()
        cnx.close()