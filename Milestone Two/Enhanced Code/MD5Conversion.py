# Troy Smith
# CS-499-H6771
# Milestone Two
# Zoo Authentication System (Converted from Java)

#This program allows a user to authenticate into the system and
#when successful authentication is acheived, the user is greeted
#with a welcome message according to their role in the system.

#Use the credentials.txt file for testing with usernames and passwords

# Imports
import sys
import hashlib


# Convert password into MD5 hash
# This function uses the hashlib library to convert the user password (string) into hash

def MD5ConversionFunc(userPassword, Type):
    password = userPassword
    userRole = Type

    hashed = hashlib.md5(password.encode())  # uses hashlib to encode hashed password

    hashed2 = hashed.hexdigest()  # returns the digest for the hashed pass; returns as string containing only -
    # hexadecimals

    passCheck(hashed2, userRole)

    return hashed2  # Returns hashed password


# Function that compares the entered password to the stored password
# The hashed passwords are stored in the lists

def passCheck(password, zooType):
    userPassword = password
    userRole = zooType

    # List to store passwords

    keeperPswrd = ["108de81c31bf9c622f76876b74e9285f", "17b1b7d8a706696ed220bc414f729ad3"]
    adminPswrd = ["3e34baa4ee2ff767af8c120a496742b5", "0d107d09f5bbe40cade3de5c71e9e9b7"]
    vetPswrd = ["a584efafa8f9ea7fe5cf18442f32b07b", "3adea92111e6307f8f2aae4721e77900"]
    coderPswrd = ["68e47349d02711aebd5dcc7478b3972d"]

    # Validate password and open the coresponding text file based on user role
    # Once authentication is successful, FileOpen is called to open the correct file

    if userPassword in keeperPswrd and userRole == "zookeeper":
        FileOpen(userRole)

    elif userPassword in adminPswrd and userRole == "admin":
        FileOpen(userRole)

    elif userPassword in vetPswrd and userRole == "veterinarian":
        FileOpen(userRole)

    elif userPassword in coderPswrd and userRole == "coder":
        FileOpen(userRole)

    else:
        print("\nInvalid Password!\n")  # If password not valid, return to login loop


# Function for opening and reading .txt files. Each file is related to one of the four user roles

def FileOpen(userFileSelect):
    if userFileSelect == "zookeeper":  # Read the zookeeper file and print text
        file1 = open("zooKeeper.txt", "r")
        print(file1.read())
        print("\n")
        LogOut()

    if userFileSelect == "admin":  # Read the admin file and print text
        file2 = open("admin.txt", "r")
        print(file2.read())
        print("\n")
        LogOut()

    if userFileSelect == "veterinarian":  # Read the veterinarian file and print text
        file3 = open("veterinarian.txt", "r")
        print(file3.read())
        print("\n")
        LogOut()

    if userFileSelect == "coder":  # Read the coder file and print text
        file4 = open("coder.txt", "r")
        print(file4.read())
        print("\n")
        LogOut()


# Logout function - Prompt user to logout or exit

def LogOut():

    logoutLoop = True

    print("Logout/return to menu or exit?")
    print("1 - Logout and return to menu")
    print("2 - Exit")

    while logoutLoop:  # Loop to ensure choice of 1 or 2

        logoutSelection = input()

        if logoutSelection == '1':
            logoutLoop = False
            main()  # Return to main function

        elif logoutSelection == '2':
            print("Goodbye!")
            sys.exit()  # Exit / terminates the program

        else:
            print("Error, please type 1 or 2\n")
            continue


# Main function - used to prompt user to login or exit

def main():
    menu = True
    attempts = 3

    print("Welcome to the authentication system.")

    while menu:  # Login loop

        print("Please enter a number to continue: \n1-Login \n2-Exit")
        menuSelection = input()

        if menuSelection == '1':  # Menu selection 1
            while attempts != 0:  # Counter to allow only 3 attempts
                print("Enter Username: ")
                userName = input()  # Store username

                print("Enter Password: ")
                userPassword = input()  # Store user password

                if userName in ["griffin.keys", "donald.monkey"]:
                    userRole = "zookeeper"  # Assigns user role zookeeper
                    MD5ConversionFunc(userPassword, userRole)  # Call md5 password conversion
                    attempts -= 1  # Attempt decrement

                elif userName in ["rosario.dawson", "bruce.grizzlybear"]:
                    userRole = "admin"
                    MD5ConversionFunc(userPassword, userRole)
                    attempts -= 1

                elif userName in ["bernie.gorilla", "jerome.grizzlybear"]:
                    userRole = "veterinarian"
                    MD5ConversionFunc(userPassword, userRole)
                    attempts -= 1

                elif userName in ["troy.smith"]:
                    userRole = "coder"
                    MD5ConversionFunc(userPassword, userRole)
                    attempts -= 1

                else:
                    print("Invalid user name!\n")
                    attempts -= 1  # Attempt counter decrement
                    print(attempts, "Attempt(s) left\n")

                    if attempts == 0:
                        print("\nOut of login attempts. Goodbye!")
                        sys.exit()  # Exits if max attempts is reached

                    continue  # Loop

            break  # Loop

        if menuSelection == '2':  # Menu selection 2

            yesNoLoop = True  # Variable for loop
            while yesNoLoop:  # Loop for yes or no choice

                print("Are you sure you want to exit? (y/n)")
                yesNo = input()

                if yesNo in ['y', 'Y']:
                    print("Goodbye!")
                    sys.exit()  # Exits if user input is upper or lowercase Y

                elif yesNo in ['n', 'N']:
                    yesNoLoop = False  # Ends loop and returns to main if user input is uppercase or lowercase N
                    main()

                else:
                    print("Error, please type y or n!")  # Error message for improper user input
                    continue # Loop
        else:
            print("\nError, please enter 1 or 2\n\n")  # Must input correct data
            continue  # Loop


if __name__ == "__main__":
    main()
