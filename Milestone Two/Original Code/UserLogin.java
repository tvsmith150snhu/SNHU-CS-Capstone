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
