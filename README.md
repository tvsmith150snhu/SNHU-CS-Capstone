# SNHU-CS-CAPSTONE
SNHU Capstone Portfolio for **Troy Smith CS-499**
There are four Milestones related to my final project for the SNHU computer science capstone.

There are three programs within the repository displaying my different computer science skills and abilities.
1. Software Design and Engineering - Transform a project into another coding language
2. Algorithms and Data Structure - Improve Efficiency 
3. Databases - Create a MongoDB using a RESTful API

## Strengths (Self Assessment)

##### Software Engineering and Security

I entered the Computer Science Program at Southern New Hampshire University in September of 2017 and continued that trek for five years while working a full-time career and supporting a family.  I have learned how computer hardware, software and applications work in concert to provide problem solving tools for small and large business and personal users as well.  At the base of these problem solving tools are well written and informatively commented code that afford computer scientists not only the ability to solve the problem, but allows others to enhance the code and make it better or more versatile to solve other problems or modernize it for future endeavors.  This explores strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science and is shown in the Software Design and Engineering artifact presented in this portfolio in which I enhance the original authentication program written in Java by writing it in Python and improving the MD5 hash function’s speed, reducing resource utilization on the computer’s hardware.  This artifact also demonstrates how I have developed a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources by creating the MD5 authentication and reducing the amount of resources necessary to run it.  This artifact presentation also includes a flowchart and demonstrated my ability to design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts.  These artifacts demonstrate my strength and ability to develop and maintain code in multiple coding languages and produce flowcharts or in some cases Pseudocode.

##### Data Structures and Algorithms

As a working professional, I hope to solidify my future as a computer scientist in my existing career and possibly advance into a more lucrative career, should the opportunity present.  As data increases and technology advances, computer scientists will prevail as pillars within most if not all industries and be necessary to contend and maintain complex business systems.  Being able to design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while maintaining  the trade-offs involved in design choices is paramount.  I demonstrate my ability to construct and work with algorithms and data structures in my Binary Search Tree algorithm artifact written in the C++ language.  The original algorithm searches files in the CSV format, while the enhanced algorithm is written in the Python language and searches an XLSX formatted file using traversal method in a more efficient manner.  These artifacts demonstrate my strength to work with algorithms and data structures as a competent computer scientist.
 

##### Databases

The ability to create, read, update and delete data within a secure and accessible database in another trait of a well-educated and versatile computer scientist.  The ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals is demonstrated in my database artifact, where I display a dashboard created for a company to utilize a Mongo database, secure that database with credentials and am able to use the CRUD (Create, Read, Update and Delete) method within it.  I then show my abilities to create an enhanced ReSTful (Representation, State, and Transfer) API using a locally hosted Mongo database that includes JSON formatted collections.  These artifacts display my strength to create and use database structures.

##### Team Environments

During my courses at SNHU, I have learned that teamwork is imperative when designing complex programs and software.  To keep the team focused and project milestones met, methodologies such as Agile were introduced and discussed during courses to introduce us to productive team concepts.  Other sharing methods, such as GitHub and Bit Bucket were introduced to provide a team sharing platform to improve and advance code.  These sites allow blame and version recovery capabilities to correct mistakes and educate team members in a constructive manner.   Exposure to these team environments and tools will benefit me as I become a productive member of a team of computer scientists.  

##### Communication to Stakeholders

The ability to communicate to stakeholders in written, oral and a visual manner is vital for a successful computer scientist.   Written communication may be in the form of comments within lines of code, readme files or a simple email.  Visual communication may be in flowcharts, diagrams or Power Point presentations.  Oral communication may be in person, in virtual meetings or in videos, such as the Code Review milestone of this portfolio.  Stakeholders may include potential employers, current superiors, customers, or other collaborators on the same team.  Communication delivered in a concise and prompt manner will benefit and promote computer scientists that utilize it in an educated manner.


## Milestone One
  This Milestone includes a recorded narative of my selection of artifacts for the portfolio, the review of the original code and my plan to enhance the code.
  
  Please enjoy my video of [Code Review](https://www.loom.com/share/1ad24d19309b48c3b39fcd978ce13a2c).
  
  
## Milestone Two
The Artifact chosen to display my work and skills learned in Software Engineering and Design is the Authentication program written in Java code and created in my IT 145 course on April 22, 2018.  This program uses the MD5 hash method to authenticate users into the Zoo Authentication System allowing them three chances before stopping any further attempts.  Once successful authentication is achieved, the user is greeted with a message according to their role in the Zoo system, which are admin, veterinarian, zookeeper or coder.  

Inclusion of this artifact in my portfolio demonstrates my ability write code in the Java language to solve problems, in this case a means to authenticate users into a specific system.  It also incorporates the Computer Science program outcome of demonstrating the ability to use well-founded and innovative techniques, skills and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry specific goals by proving my worth as a computer scientist that has the skills to code in Java and then transform that language into Python for the enhancement portion of the project.  I achieved this in the enhanced code by reducing the lines of code and containing all the necessary methods within the main function, instead of multiple files, demonstrating innovative technique, skills and tools. I have the skills to develop the code in a readable and transformable format that may be built upon for further enhancement alone, by someone else or within a team and possess the traits of a promising new computer scientist.

I have enhanced the program by writing it in the Python language and condensing it into less lines of code in one file instead of multiple files with more lines of code.  The original code also required the program to completely exit or stop before another user could authenticate.  The enhanced Python code allows the program to continue to run and allow another user to authenticate into the system.  

Python was the language used in my first introduction to coding in my CS 200 course in 2017 and has continued to intrigue me as an easy to read language that is versatile enough to be used in many different problem solving situations.  Although still new to coding and learning more each time I code, I find Python to be a very legible and straight forward language.  

The original code had to be updated when files were moved or ran on other systems with a different file directory.  Often errors occurred when the file could not be found.  I learned this was not the case with the enhanced version and the Python code – the files opened flawlessly and less lines of code meant less work.  The enhanced version does include the usernames within the code presenting somewhat of a security risk, but the passwords are kept hidden with the MD5 hash method.  The original code kept the usernames and passwords in a separate credentials file that could be hidden or protected for security purposes.  The argument could be made to keep the entire code hidden for both the Java and Python code in that regard.

Most of the challenge in enhancing the code was recalling the nuances of the Python language that I hadn’t used in quite a while.  Having a full time career while obtaining my Bachelor’s degree has resulted in taking one course at a time over the span of five years.  That leaves gaps in the last time I coded or used certain skills.  Thankfully reviewing my notes and visiting site on the web and watching videos brought back enough remembrance to get me through the challenge.   
   
  
  ![image](https://user-images.githubusercontent.com/85906554/180590138-162ecfea-9cde-4ca8-a426-f58cb9a18172.png)
  
 ## Java Code:

```

/*Troy Smith
 *IT-145-X4663
 *Final Project
 *Option 1: Authentication System
 *April 22, 2018
 */

/*This program authenticates a user with the MD5 hash method
 *The user is greeted with message from a text file 
 * according their role within the system.
 * The user is granted 3 tries before the system exits
 * and notifies them they have failed to authenticate.
 */

package zooauthentication;
//Import libraries and classes
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;
import static zooauthentication.UserRole.printAdminRole;
import static zooauthentication.UserRole.printCoderRole;
import static zooauthentication.UserRole.printVetRole;
import static zooauthentication.UserRole.printZooKeepRole;

public class UserLogin {
    //Method used to prompt user for login information
    public static void loginPrompt() {
        //Declare string variable for user input
        String userInput;
        //Import scanner for user input
        Scanner scanr4input = new Scanner(System.in);       
        //Post welcome message, then prompt user to Login or Exit
        System.out.println("********************************************");
        System.out.println("* Welcome to the Zoo Authentication System *");
        System.out.println("********************************************");
        System.out.println("Enter \"LOGIN\" to use the system, or");
        System.out.println("Enter \"EXIT\" to exit the system: ");
        userInput = scanr4input.nextLine();
        //Allow user to exit system
        if (userInput.equalsIgnoreCase(
                "EXIT")) {
            System.exit(0);
        }
        //Prevent user from entering random text.  Must enter "EXIT" or "LOGIN"
        while (!userInput.equalsIgnoreCase("LOGIN")) {
            System.out.println("INVALID INPUT!  Enter \"EXIT\" or \"LOGIN\": ");
            userInput = scanr4input.nextLine();
            if (userInput.equalsIgnoreCase(
                    "EXIT")) {
                System.exit(0);
            }
        }
        //Declare String Variable for user password
        String usrPswrd;
        //Declare flag to control flow in loops
        boolean validUser = false;
        //Declare variable to limit number of login attempts
        int numTries = 3;
        //Create scanner object to read credentials.txt file
        BufferedReader credScanr = new BufferedReader(new InputStreamReader(System.in));
        
        //Prompt user for username and password
        //Loop for login attempts
        try {

            do {
                //Decrement number of attempts to login
                numTries--;
                //Username prompt
                System.out.println("\nEnter Username or \"EXIT\" to quit: ");
                //Get username from scanner input
                String userName = credScanr.readLine();
                //Loop to provide exit before attempts to 
                if (userName.equalsIgnoreCase(
                        "EXIT")) {
                    System.exit(0);
                }
                //Password prompt
                System.out.println("Enter Password: ");
                //Get username from scanner input
                String password = credScanr.readLine();
                //Convert password using MD5 hash
                MessageDigest md123 = MessageDigest.getInstance("md5");

                md123.update(password.getBytes());

                byte[] bytes12 = md123.digest();

                StringBuilder sb1 = new StringBuilder();
                for (byte b : bytes12) {
                    sb1.append(String.format("%02x", b & 0xff));
                }

                usrPswrd = sb1.toString();
                //Declares variable from lines of text in credentials.txt file
                String credFileLine;
                //Open credentials.txt file
                BufferedReader credFile = new BufferedReader(new FileReader("G:\\My Drive\\SNHU\\IT145\\Final Project\\ZooAuthentication\\ZooAuthentication\\src\\zooauthentication\\credentials.txt"));
                //Loop to find MD5 hash text
                while ((credFileLine = credFile.readLine()) != null) {
                    //Create array with line containing MD5 hash
                    String[] lineINcredfile = credFileLine.split("\t");
                    //Parse username in credentials.txt file
                    if (lineINcredfile[0].equals(userName)) {
                        //Parse password in credentials.txt file
                        if (lineINcredfile[1].equals(usrPswrd)) {
                            //Flag determines true if MD5 hash was found
                            validUser = true;
                            //Exit loop
                            break;
                        }
                    }
                }
                
                //Loop to search for user roles in credentials.txt file
                if (validUser == true) {
                    //Call method in UserRole class for admin.txt file
                    if (credFileLine.contains("admin")) {
                        //Call printAdminRole in UserRole class
                        printAdminRole();
                    }
                    //Call method in UserRole class for veterinarian.txt file
                    if (credFileLine.contains("veterinarian")) {
                        //Call printVetRole in UserRole class
                        printVetRole();
                    }
                    //Call method in UserRole class for zookeeper.txt file
                    if (credFileLine.contains("zookeeper")) {
                        //Call printZooKeepRole in UserRole class
                        printZooKeepRole();
                    }
                    //Call method in UserRole class for coder.txt file
                    if (credFileLine.contains("coder")) {
                        //Call printZooKeepRole in UserRole class
                        printCoderRole();
                    }
                    break;

                } else {
                    //Notify user if login attempt fails
                    System.out.println("\nInvalid Username or Password.");
                    //Encourage user to keep going
                    System.out.println(" Try again.");
                    //Notify user of number of attempts remaining (3,2,1)
                    System.out.println(numTries + " more attemptes remain.");
                    //Loop condition to terminate login attempts
                if (numTries == 0) {
                    //Print user notification of excessive attempts
                    System.out.println("\nMAX attempts exceeded!");

                    System.out.println(" Exiting ...");
                    //Exit command
                    System.exit(0);
                }
                }
              //Stopping point for login attempts
            } while (numTries > 0);
          //Exception handler if credentials file fails to open
        } catch (NoSuchAlgorithmException | IOException e1) {
            System.out.println("\nFILE \"credentials.txt\" NOT FOUND!");
            System.out.println("Please update line 93 of UserLogin class to correct path\n");
        }
    }
}

```

## Python Code:

```

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
    
```


## Milestone Three
The Artifact I have chosen to display my work and skills learned in Algorithms and Data Structure is Binary Search Tree Algorithm from my CS 260 course on February 16, 2020.  The program reads from a CSV file and uses the algorithm to search the data listed within the file.  It then uses a linked list to store the data to sort and search it.  

Inclusion of this artifact in my portfolio demonstrates my understanding of algorithms and data structure within the C++ coding language and provides evidence of the expected outcome of the Computer Science program by proving my ability to design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practice standards appropriate to its solution, while managing the trade-offs involved in design choices.  I achieved this in my enhanced artifact by coding the new algorithm to decrease time and increase speed by using Python’s traversal method and reducing the number of lines of code.  The new code interacts with live data in a more modern XLSX format opposed to the CSV format by the original code.

I have enhanced the artifact by using the algorithm and data structure in a similar manner within the Python language and using a traversal method also.  The original code accessed a CSV file, while the enhanced use of the algorithm accesses an Excel sheet in the XLSX format allowing the user to select from a menu of choices to display the items already in the file, add a linked list of data, add items to the spreadsheet, traverse or access the Binary tree in pre order, inversely or in order and then exit the program.  This code is useful in creating user lists of any kind to store items within an Excel document and allows the user to add to the provided excel list within two columns – one with the name of the item and the other with the quantity of that item in an Items List.  

The data structures used in the code are a singly linked list and a binary tree.  The singly linked list uses one append method to append the beginning or front and uses nodes to traverse through the elements of data by setting the pointer to the consecutive or next node.  The binary tree algorithm allows the user to add ten items to the root and contains the left and right pointers as well, which connect each child branch on either side of the tree. The nodes are then created by comparing the value of the higher branch on the tree or the parent nodes.  The Python coding language uses three traversals of the binary tree – pre-order, in-order and post-order (reversal) within the program. The C++ language is more complex in memory usage in the utilization of pointers in comparison to the Python language, as Python uses a more “pre-determined” and easier method of implementing these data structures.

Python was the language used in my first introduction to coding in my CS 200 course in 2017 and has continued to intrigue me as an easy to read language that is versatile enough to be used in many different problem solving situations.  Although still new to coding and learning more each time I code, I find Python to be a very legible and straight forward language.  This project introduced me to using the Pandas library and some of its functions reading and writing to MS Excel type files that are useful to store items.  

Challenges faced in this project were recalling how to configure the Eclipse IDE in the Windows environment, then discovering the Visual Studio Code IDE and configuring openpyxl, xlsxwriter and xlrd packages within it.  I first contacted Professor John Watson from the CS 260 course who graciously sent the configurations page that I failed to save from the original course that explained how to set up Eclipse in Windows for the original code.  However, during my wait for his email reply, I discovered my MacBook Air could run the code in Eclipse without any special configuration of the IDE!  This surprised me because I replaced the MacBook since the course.  Thankfully I allowed the MacBook to update from the previous one and it actually had the program stored in history!  Even so, I needed another IDE that was versatile and provided a better environment for the Python enhanced code.  I quickly discovered the Visual Studio Code IDE (not to be confused with Visual Basic Studio) and its intuitive qualities, but struggled to get the openpyxl, xlsxwriter and xlrd packages configured within that environment on both the Mac and Windows platforms.  After a few YouTube video and Stack Overflow tutorials I was in business!  I was able to compile the enhanced code and see the algorithm and data structure work as planned and then open the MS Excel worksheet to see the items I added to the list from the user choice menu.

This artifact and its enhancement meets the course objectives in innovative skills and techniques used for accomplishing my goals by displaying how I am able to implement algorithms and data structures to write and read from the Excel Workbook using intuitive user input from the code that is kept clean and legible in a manner that other computer scientists can review and improve.  It solves user problems by allowing them to add data to the worksheet from within the program using libraries such as Pandas that uses openpyxl to write to the xlsx format.   Overall this project gave me a better understanding of data structures and algorithms and how to use them to provide solutions and solve problems.



## Milestone Four
**Artifact Selection**

The Artifact I have chosen to display my ability to store, manipulate and access data within a database is the one from my CS 340 course on October 18, 2021.  The code worked within a provided Mongo database hosted on a Virtual Machine within the course.  I also constructed code to provide a dashboard that accessed the database and referenced maps in correlation to the data.  

**Reason for Inclusion**

Databases are included in most applications, websites and systems used throughout many industries and are required to be protected and maintained by Computer Scientists that are well equipped to handle the tasks.  Inclusion of this database artifact in my portfolio demonstrates my ability to do just that and prove my worth and skills within database work and my ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.  I accomplished in both the original artifact and the enhanced artifact by developing a CRUD mongo DB allows users to create, read, update and delete items within collections contained within the database models.  The original artifact also uses authentication methods to develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources. 
 
This is an example of me create an account within a Mongo DB for an administrator and user within a terminal.

Administrative:
![image](https://user-images.githubusercontent.com/85906554/181065451-c878381b-de7b-4216-9b83-611245b35374.png)

User:
![image](https://user-images.githubusercontent.com/85906554/181067208-99818685-dbb8-4152-8c22-6dc91dff298b.png)

Here I create a Python test script that imports a CRUD Python module to call and test the ‘create’ and ‘read’ functionality.
![image](https://user-images.githubusercontent.com/85906554/181067454-49b4e9cc-a7e0-4aee-b2df-8973e6de7dc3.png)
![image](https://user-images.githubusercontent.com/85906554/181067513-ec61d289-ae8f-4dc1-bf93-5a3841e8d2eb.png)

![image](https://user-images.githubusercontent.com/85906554/181067584-de025b43-59a7-4e3d-b606-c62f80a35229.png)

And add new Item (Create)
![image](https://user-images.githubusercontent.com/85906554/181067767-81e70a0c-eafc-4ff2-bdc9-ce8192b2cf0f.png)

Update an item (Update)
![image](https://user-images.githubusercontent.com/85906554/181067847-cede0e2c-9840-4a97-ab16-bf45ea7f8c09.png)

Search for an Item (Read)
![image](https://user-images.githubusercontent.com/85906554/181067917-e51b869d-a843-4548-8c72-a3986935cc6e.png)

Remove an item (Delete)
![image](https://user-images.githubusercontent.com/85906554/181067992-60380d72-834d-4e97-a733-27036d7a82b3.png)

Here are examples of data visualization using the dashboard code found within the Project Two Dashboard file.
![image](https://user-images.githubusercontent.com/85906554/181068111-844134c5-dcb5-46fe-995e-8f5e959a2925.png)

![image](https://user-images.githubusercontent.com/85906554/181068167-cb7c3dc2-eeed-455b-b3cc-904be0070958.png)

![image](https://user-images.githubusercontent.com/85906554/181068224-d60125ee-d839-490e-b6a0-228222ff76e7.png)

![image](https://user-images.githubusercontent.com/85906554/181068279-02d2593f-87fb-4da7-af63-00803d9baf45.png)

![image](https://user-images.githubusercontent.com/85906554/181068310-57598464-ec5d-4ea9-8584-6219ef9640ae.png)

![image](https://user-images.githubusercontent.com/85906554/181068352-18414d31-b242-40b9-b45e-1c270ee2cd68.png)

![image](https://user-images.githubusercontent.com/85906554/181068376-ea197883-3956-4031-8d85-5a11b44a0897.png)


**Enhancement**

For the enhancement portion of this project, I chose to create a RESTful API that creates and accesses a Mongo DB.  REST stands for Representation, State, Transfer or basically the same as CRUD.  I utilized the features of the Visual Studio Code IDE to construct and manipulate the database hosted on the local device using port 3000.

Here is an example of the successful connection to the database.

![image](https://user-images.githubusercontent.com/85906554/181068705-70dd030c-ceb7-4e01-bac2-c9d1d82eeaaf.png)

![image](https://user-images.githubusercontent.com/85906554/181068768-27bf526c-ba74-46de-981c-eec1419fc31b.png)

Accessing items within the database.

![image](https://user-images.githubusercontent.com/85906554/181068875-b25fc8f7-5ac6-401b-915b-09bf9e47a740.png)

Creating one within the database.

![image](https://user-images.githubusercontent.com/85906554/181068959-04a6be2d-aaa1-44be-bfde-4786a4a7f82c.png)


**Course Objectives**

This project met me course objective from Module One by displaying my skills and abilities to work with and within databases.  I consider it a valuable inclusion in my portfolio and learned more than I anticipated during its construction. .  Inclusion of this database artifact in my portfolio demonstrates my ability to do just that and prove my worth and skills within database work and my ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.  I accomplished in both the original artifact and the enhanced artifact by developing a CRUD mongo DB allows users to create, read, update and delete items within collections contained within the database models.  The original artifact also uses authentication methods to develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources. 


**Challenges and Lessons Learned**

This was my first time working with the REST API and was impressed with the Visual Studio Code’s ability to intuitively install necessary and helpful extensions at will.  It included the REST client that allowed me to run my .rest commands in a real-time mode to see the results immediately and included all the necessary components to construct my code.

There weren’t as many challenges as I first anticipated, but one in particular was coding the server file correctly and getting the expected “Server Started” and “Connected to Database” prompt.  Thankfully after reviewing several YouTube videos and searching Stack Overflow posts, I successfully started the server and proceeded with the other code.  

In the end, I learned much more about REST and how it operates within the VS Code IDE.  I consider the VS Code to be my new favorite IDE!



