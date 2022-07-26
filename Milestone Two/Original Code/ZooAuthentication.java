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

//Allows method in UserLogin class
import static zooauthentication.UserLogin.loginPrompt;

//Define class
public class ZooAuthentication {

    //Define main class
    public static void main(String[] args) {
        //Call method loginPrompt in UserLogin class
        loginPrompt();
    }
}
