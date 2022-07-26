//============================================================================
// Name        : Lab1-3.cpp
// Author      : Troy Smith
// Version     : 1.0
// Date        : January 12, 2020
// Copyright   : Copyright © 2017 SNHU COCE
// Description : Lab 1-3 Up to Speed in C++
//============================================================================

#include <algorithm>
#include <iostream>

using namespace std;

//============================================================================
// Global definitions visible to all methods and classes
//============================================================================

// Forward declarations
double strToDouble(string str, char ch);

// Data structure to hold bid information together as a single unit of storage.
struct chosenBid {
	string title;
	string fund;
	string vehicle;
	double amount;
};

// Bid values passed in data structure
/**
 * Display the bid information
 */
void displayBid(chosenBid bid) {
    cout << "Title: " << bid.title << endl;
    cout << "Fund: " << bid.fund << endl;
    cout << "Vehicle: " << bid.vehicle << endl;
    cout << "Bid Amount: " << bid.amount << endl;

    return;
}

// Store input values in data structure
/**
 * Prompt user for bid information
 *
 * @return data structure containing the bid info
 */
chosenBid getBid() {
    chosenBid userBid;

    cout << "Enter title: ";
    cin.ignore();
    getline(cin, userBid.title);

    cout << "Enter fund: ";
    cin >> userBid.fund;

    cout << "Enter vehicle: ";
    cin.ignore();
    getline(cin, userBid.vehicle);

    cout << "Enter amount: ";
    cin.ignore();
    string strAmount;
    getline(cin, strAmount);
    userBid.amount = strToDouble(strAmount, '$');

    return userBid;
}

/**
 * Simple C function to convert a string to a double
 * after stripping out unwanted char
 *
 * credit: http://stackoverflow.com/a/24875936
 *
 * @param ch The character to strip out
 */
double strToDouble(string str, char ch) {
    str.erase(remove(str.begin(), str.end(), ch), str.end());
    return atof(str.c_str());
}


/**
 * The one and only main() method
 */
int main() {

    // Declared instance of data structure to hold bid information
	chosenBid placedBid;

    // loop to display menu until exit chosen
    int choice = 0;
    while (choice != 9) {
        cout << "Menu:" << endl;
        cout << "  1. Enter Bid" << endl;
        cout << "  2. Display Bid" << endl;
        cout << "  9. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;

        // Method calls
        switch (choice) {
            case 1:
            	placedBid = getBid();
                break;
            case 2:
                displayBid(placedBid);
                break;
        }
    }

    cout << "Good bye." << endl;

    return 0;
}
