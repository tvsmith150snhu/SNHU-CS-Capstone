/*Troy Smith
 *IT-145-X4663
 *Final Project
 *Option 1: Authentication System
 *April 22, 2018
 */
package zooauthentication;
//Import scanner for user input
import java.util.Scanner;
//Allows calls to UserLogin class
import static zooauthentication.UserLogin.loginPrompt;
//Declare class
public class UserLogout {
    //Declare method
    public static void logoutPrompt() {
        //Declare String of exit command
        String exitCmd;
        //Create scanner object for user input
        Scanner scanr4input = new Scanner(System.in);
        //Prompt user how to log out
        System.out.println(
                "\nEnter \"EXIT\" to logout");
        exitCmd = scanr4input.nextLine();        
        //Prevent user from entering random text.  Must enter "EXIT" to logout
        while (!exitCmd.equalsIgnoreCase("EXIT")) {
            System.out.println("INVALID INPUT!  You may only enter \"EXIT\": ");
            exitCmd = scanr4input.nextLine();
            if (exitCmd.equalsIgnoreCase(
                    "EXIT")) {
                System.out.println("Logging out . . . have a great day!\n");
                //Moves back to method loginPrompt in UserLogin class to start over
                loginPrompt();
            }
        }
    }

}
