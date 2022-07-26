# SNHU-CS-CAPSTONE
SNHU Capstone Portfolio for **Troy Smith CS-499**
There are four Milestones related to my final project for the SNHU computer science capstone.

There are three programs within the repository displaying my different computer science skills and abilities.
1. Software Design and Engineering - Transform a project into another coding language
2. Algorithms and Data Structure - Improve Efficiency 
3. Databases - Create a MongoDB using a RESTful API

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



