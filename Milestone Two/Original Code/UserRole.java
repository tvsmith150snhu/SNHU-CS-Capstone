/*Troy Smith
 *IT-145-X4663
 *Final Project
 *Option 1: Authentication System
 *April 22, 2018
 */
package zooauthentication;
//Import libraries for method functions
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import static zooauthentication.UserLogout.logoutPrompt;

//Define class
public class UserRole {
    //Method that will print text from admin.txt file
    public static void printAdminRole() throws FileNotFoundException, IOException {
        //Add line to seperate output from user input
        System.out.print("\n");
        //Open admin.txt file, read that file and print text from it
        try (FileReader adminFile = new FileReader("/Users/troysmith/Library/Mobile Documents/"
                + "com~apple~CloudDocs/SNHU/Courses/18EW4/IT-145-X4663/Java Projects/"
                + "ZooAuthentication/src/zooauthentication/admin.txt");
                BufferedReader br = new BufferedReader(adminFile)) {
            String buffer;
            String fulltext = "";
            while ((buffer = br.readLine()) != null) {
                System.out.println(buffer);
                fulltext += buffer;
            }
        }
        //Exception handler if admin.txt file fails to open
        catch (IOException e1) {
            System.out.println("\nFILE \"admin.txt\" NOT FOUND!");
            System.out.println("Please update line 22 of UserRole class to correct path\n");
        }
        //Calls to logoutPrompt in UserLogout class
        logoutPrompt();
    }
    //Method that will print text from veterinarian.txt file
    public static void printVetRole() throws FileNotFoundException, IOException {

        //Add line to seperate output from user input
        System.out.print("\n");

        //Open veterinarian.txt file, read that file and print text from it
        try (FileReader vetFile = new FileReader("/Users/troysmith/Library/Mobile Documents/"
                + "com~apple~CloudDocs/SNHU/Courses/18EW4/IT-145-X4663/"
                + "Java Projects/ZooAuthentication/src/zooauthentication/veterinarian.txt");
                BufferedReader br = new BufferedReader(vetFile)) {
            String buffer;
            String fulltext = "";
            while ((buffer = br.readLine()) != null) {
                System.out.println(buffer);
                fulltext += buffer;
            }
        }
        //Exception handler if veterinarian.txt file fails to open
        catch (IOException e1) {
            System.out.println("\nFILE \"veterinarian.txt\" NOT FOUND!");
            System.out.println("Please update line 48 of UserRole class to correct path\n");
        }
        //Calls to logoutPrompt in UserLogout class
        logoutPrompt();
    }
    //Method that will print text from zookeeper.txt file
    public static void printZooKeepRole() throws FileNotFoundException, IOException {

        //Add line to seperate output from user input
        System.out.print("\n");

        //Open zookeeper.txt file, read that file and print text from it
        try (FileReader zooKeepFile = new FileReader("G:\\My Drive\\SNHU\\IT145\\Final Project\\ZooAuthentication\\ZooAuthentication\\src\\zooauthentication\\zookeeper.txt");
                BufferedReader br = new BufferedReader(zooKeepFile)) {
            String buffer;
            String fulltext = "";
            while ((buffer = br.readLine()) != null) {
                System.out.println(buffer);
                fulltext += buffer;
            }
        //Exception handler if zookeeper.txt file fails to open
        } catch (IOException e1) {
            System.out.println("\nFILE \"zookeeper.txt\" NOT FOUND!");
            System.out.println("Please update line 74 of UserRole class to correct path\n");
        }
        //Calls to logoutPrompt in UserLogout class
        logoutPrompt();
    }
    //Method that will print text from coder.txt file
    public static void printCoderRole() throws FileNotFoundException, IOException {

        //Add line to seperate output from user input
        System.out.print("\n");

        //Open zookeeper.txt file, read that file and print text from it
        try (FileReader zooKeepFile = new FileReader("/Users/troysmith/Library/"
                + "Mobile Documents/com~apple~CloudDocs/SNHU/Courses/18EW4/"
                + "IT-145-X4663/Java Projects/ZooAuthentication/src/"
                + "zooauthentication/coder.txt");
                BufferedReader br = new BufferedReader(zooKeepFile)) {
            String buffer;
            String fulltext = "";
            while ((buffer = br.readLine()) != null) {
                System.out.println(buffer);
                fulltext += buffer;
            }
        //Exception handler if zookeeper.txt file fails to open
        } catch (IOException e1) {
            System.out.println("\nFILE \"coder.txt\" NOT FOUND!");
            System.out.println("Please update line 99 of UserRole class to correct path\n");
        }
        //Calls to logoutPrompt in UserLogout class
        logoutPrompt();
    }


}

