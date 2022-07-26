# Troy Smith
# CS-499-H6771
# Data Structures and Algorithms
# Milestone 3
# 2022.07.24

# Requires openpyxl, xlsxwriter, and xlrd packages
# The data structures shown here are a singly linked list and a binary tree

# This program reads from the 'ItemList.xlsx' file and Traversal in Binary Tree
# It allows the user to add items and amounts to the ItemList
# Please ensure the 'ItemsList.xlsx' file is closed and not accessed by another program


import sys
import pandas as pd
from openpyxl import load_workbook
from pip._vendor.distlib.compat import raw_input


# Class for linked list - Creates node containing head and next pointer

class node:
    def __init__(self, data=None):  # 'Constructor'
        self.data = data
        self.next = None


# Linked list class - Contains linked list print and add node
# Nodes are added to the front of the list instead of the back

class linkedList:
    def __init__(self):  # 'Constructor'
        self.head = node()  # head node
        self.tail = None  # Tail set to none
        self.length = 0  # Length

    # Add node to the front

    def addNodeF(self, newData):
        newNode = node(newData)

        # New node added to the head of the list

        newNode.next = self.head
        self.head = newNode

    # For printing linked list

    def printList(self):
        pn = self.head  # set head
        while pn:
            print(pn.data)  # print data
            pn = pn.next  # set to next


# Class for binary tree and search

class treeNode:
    def __init__(self, data=None):  # Constructor
        self.data = data
        self.left = None  # left branch
        self.right = None  # right branch

    # Create the tree - left and right nodes

    def addTree(self, data=None):
        if data == self.data:
            return

        # left branches (child)

        if data < self.data:
            if self.left is None:
                self.left = treeNode(data)
            else:
                self.left.addTree(data)

        # right branches (child)

        else:
            if self.right is None:
                self.right = treeNode(data)
            else:
                self.right.addTree(data)

    # Tree traversal
    # Pre order traversal

    def traversal(self, root=None):
        elements = []  # list of elements
        if root:
            elements.append(root.data)  # current node
            elements += self.traversal(root.left)  # traverse left branch from root
            elements += self.traversal(root.right)  # traverse right branch from root

        return elements  # Return list of elements

    # Reverse order traversal

    def postTraversal(self, root=None):
        elements = []
        if root:
            elements = self.postTraversal(root.left)  
            elements += self.postTraversal(root.right) 
            elements.append(root.data)

        return elements

    # Forward order traversal

    def inTraversal(self, root=None):
        elements = []
        if root:
            elements = self.inTraversal(root.left) 
            elements.append(root.data)
            elements += self.inTraversal(root.right)

        return elements


# Tree function for user input
# Accept user input and inserts into nodes or leaves

def userTreeSearchPost():
    menuLoop = True
    root = treeNode("Root")  # Assign root node

    while menuLoop is True:  # menu loop

        print("Tree root is called 'Root'")
        print("Would you like to add a new leaf? (y/n)")
        yesNo = input()

        if yesNo in ["y", "Y"]:

            # Loop for user to enter 10 'objects' which will be put into the binary tree
            print("Enter 10 items: ")
            for i in range(10):
                tree = raw_input()
                root.addTree(tree)

            print("\n")
            print(root.postTraversal(root), "\n")  # Traversal for viewing the tree
            menuLoop = False  # Stop menu loop

        elif yesNo in ["n", "N"]:
            menuLoop = False  # Stop menu loop

        else:
            print("Error, please enter y or n\n")
            continue  # Ensure proper input


# Inverse traversal tree function

def userTreeSearchIn():
    menuLoop = True
    root = treeNode("Root")  # Assign root node

    while menuLoop is True:  # Menu loop

        print("Tree root is word 'Root' - Branches are created alphabetically")
        print("Would you like to add a new leaf? (y/n)")
        yesNo = input()

        if yesNo in ["y", "Y"]:

            # Loop for user to enter 10 'items' which will be put into the binary tree

            print("Enter 10 items: ")
            for i in range(10):
                tree = raw_input()
                root.addTree(tree)

            print("\n")
            print(root.inTraversal(root), "\n")  # Traversal for viewing tree
            menuLoop = False  # Stop menu loop

        elif yesNo in ["n", "N"]:
            menuLoop = False  # Stop menu loop

        else:
            print("Error, please enter y or n\n")
            continue  # Ensure proper input


# This function is for the binary tree but uses the Items and Amounts data from the spreadsheet
# It primarily shows that the data from the spreadsheet can be stored in a data structure

def treeSearchitems(itemData, amountData):
    items = itemData
    amounts = amountData

    itemstring = " ".join(map(str, items))  # Convert to String
    amountString = " ".join(map(str, amounts))

    #     root
    #    /    \
    #  items  amounts

    root = treeNode("Root")  # Set Root node
    root.addTree(itemstring)  # Use item data for node
    root.addTree(amountString)  # Use amount (quantity) data for node

    print("\n")
    print(root.traversal(root), "\n")  # Traversal for viewing tree



# Function for traversing the linked list
# Data is lost after program terminates.  It simple shows that 
# The algorighm can combine user input and the spreadsheet data

def listSearch(itemData, amountData):
    menuLoop = True
    items = itemData
    amounts = amountData
    lst1 = []  # List for items and amounts

    list1 = linkedList()
    list1.head = node(items)  # head node is set to the items in the spreadsheet
    n2 = node(" ")  # and white space
    n3 = node(amounts)  # node 3 for the amounts

    # Set node and list order

    list1.head.next = n2
    n2.next = n3

    while menuLoop is True:  # loop

        print("Would you like to add a new node? (y/n)")
        yesNo = input()

        if yesNo in ["y", "Y"]:

            # Iterates ten times for user objects
            # These objects are saved to a list

            print("Enter new node: ")
            print("Enter 10 objects: ")
            for i in range(10):
                n4 = raw_input()  # Takes input for list
                lst1.append(n4)  # Append the list

            list1.addNodeF(lst1)  # Places the list in the first node
            list1.printList()  # Display the linked list
            print("\n")
            menuLoop = False  # Stop loop

        elif yesNo in ["n", "N"]:
            list1.printList()  # Display linked list without user data
            print("\n")
            menuLoop = False  # Stop loop

        else:
            print("Error, please enter y or n\n")
            continue  # Ensure proper input


# This function is used to append data to the excel spreadsheet
# I found this append information from -
# https://medium.com/better-programming/using-python-pandas-with-excel-d5082102ca27
# In this function the user's data is added to the spreadsheet

def addData():
    addLoop = True

    while addLoop:  # Loop for y/n selection

        print("Please type the name of the item: ")
        userItem = input()  # Input for the item

        print("How many? ")
        userAmount = input()  # Input for the quantity

        # Data frame for adding data to the excel spreadsheet
        df2 = pd.DataFrame({"items": [userItem], "Amounts": [userAmount]})

        # Use openpyxl to write to file
        writer = pd.ExcelWriter("ItemList.xlsx", engine="openpyxl", mode='a', if_sheet_exists='overlay')

        # Load spreadsheet as workbook
        writer.book = load_workbook("ItemList.xlsx")

        # Copy the current spreadsheet
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)

        # Read the Excel file
        reader = pd.read_excel(r'ItemList.xlsx')

        # Write to the spreadsheet
        df2.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

        # Cease inputs
        writer.close()

        print("Data added\nAdd more data? (Y/N)")

        # Choice to add more data or return to menu
        yesNo = input()

        if yesNo in ['y', 'Y']:
            continue  # loop again

        elif yesNo in ['n', 'N']:
            addLoop = False  # Stop loop
            main()  # the one and only main method
        else:
            print("Error, Returning to menu\n")
            break  # Exit loop


# Main function
# Contains the intro menu loop and pandas
# to read the spreadsheet and convert it to a list

def main():
    # Import the data sheet from Excel

    # Pandas reads the Excel spreadsheet and assigns it to a variable

    df2 = pd.read_excel("ItemList.xlsx", header=None, names=["items", "Amounts"])

    # The two main columns are converted to lists (Items and Amounts)
    # The variables are also declared here to be passed to other functions

    items = df2["items"].values.tolist()
    amounts = df2["Amounts"].values.tolist()
    print("Data Loaded Successfully!\n")

    menuLoop = True
    yesNoLoop = True

    #Consider dropping menu items that currupt spreadsheet
    while menuLoop is True:  # Loop for Menu
        print("******************")
        print("*---User Menu---*")
        print("******************")
        print("Please Make a Choice")
        print("1: Display Spreadsheet Items")
        print("2: Add Node of Linked List Data")
        print("3: Add Items to Spreadsheet")
        print("4: Binary Tree - Pre Order Traversal with Spreadsheet Data")
        print("5: Binary Tree - Inverse Traversal with User Data")
        print("6: Binary Tree - In order Traversal with User Data")
        print("9: Exit")

        menuChoice = input()

        # Menu choices and passes to functions

        if menuChoice == "1":

            # uses zip to pair tuples
            # This is how to get items and amounts lined up together
            for a, b in zip(items, amounts): 
                print(a, b, )
            print("\n")

        elif menuChoice == "2":
            listSearch(items, amounts)

        elif menuChoice == "3":
            addData()

        elif menuChoice == "4":
            treeSearchitems(items, amounts)

        elif menuChoice == "5":
            userTreeSearchPost()

        elif menuChoice == "6":
            userTreeSearchIn()

        elif menuChoice == "9":

            while yesNoLoop is True:

                exitChoice = input("Exit? (y/n): ")

                if exitChoice in ["y", "Y"]:
                    print("Goodbye!")
                    sys.exit()

                elif exitChoice in ["n", "N"]:
                    yesNoLoop = False
                    main()

                else:
                    print("Error, please type y or n!")
                    continue

        else:
            print("Error")
            continue


if __name__ == '__main__':
    main()
