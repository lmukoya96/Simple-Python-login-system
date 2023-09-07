import mysql.connector
from mysql.connector import errorcode

class User:
    def get_personal_info():
        # Prompt user for personal information
        first_name = input("Enter your First Name: ")
        last_name = input("Enter your Last Name: ")
        date_of_birth = input("Enter your date of birth (DD-MM-YYYY): ")
        phone_number = input("Enter your Phone Number: ")
        country = input("Enter your Country: ")
        street = input("Enter your Street: ")
        city = input("Enter your City: ")
        state = input("Enter your State: ")
        email = input("Enter your Email: ")
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        
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
            "Password": password
        }
        
        return personal_info


    def store_personal_info(personal_info):
        try:
            # Connect to the MySQL server
            cnx = mysql.connector.connect(
                host="your_connection",
                user="your_username",
                password="your_password",
                database="simple_softwaredb"
            )

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                # The database does not exist, so create it
                cnx = mysql.connector.connect(
                    host="your_connection",
                    user="your_username",
                    password="your_password",
                )
                cursor = cnx.cursor()

                # Create the database
                cursor.execute("CREATE DATABASE simple_softwaredb")
                cursor.execute("USE simple_softwaredb")
                cursor.execute("CREATE TABLE personal_info (first_name TEXT(255), last_name TEXT(255), date_of_birth DATE, phone_number VARCHAR(15), country TEXT(255), street TEXT(255), city TEXT(255), state TEXT(255), email VARCHAR (50), username TEXT(255), password TEXT(255))")          
                cnx.database = "simple_softwaredb"

            else:
                print("Error connecting to MySQL server:", error)
                return

        finally:
            if 'cursor' in locals():
                cursor.close()

        try:
            # Connect to the MySQL database
            cnx = mysql.connector.connect(
                host="your_connection",
                user="your_username",
                password="your_password",
                database="simple_softwaredb"
            )

            # Create a cursor object to interact with the database
            cursor = cnx.cursor()

            # Define the SQL query
            query = """
            INSERT INTO personal_info (first_name, last_name, date_of_birth, phone_number, country, street, city, state, email, username, password)
            VALUES (%(First Name)s, %(Last Name)s, %(Date of Birth)s, %(Phone Number)s, %(Country)s, %(Street)s, %(City)s, %(State)s, %(Email)s, %(Username)s, %(Password)s)
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