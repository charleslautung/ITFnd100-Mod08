# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CLTUNG, June 2, 2021,Modified code to complete assignment 8
# CLTUNG, June 2, 2021, Added Product Class with Constructor and Getter/Setter
# for Product Name and Price
# CLTUNG, June 2, 2021, Added Process Class with Constructor and Getter/Setter
# to Process Data
# CLTUNG, June 2, 2021, Added IO Class for Input and Output
# CLTUNG, June 2, 2021, Added Main Event Loop
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstTable = []
strChoice = ""
strStatus = ""

class Product:
    """Stores data about a product:

    properties:
        prod_name: (string) with the products's  name
        price: (float) with the products's standard price
    methods:
        property:  Getter for Product Name

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # --Constructor--
    def __init__(self, prod_name, price):
        self.__prod_name = prod_name
        self.__price = price

    # -- Properties --
    # Product Name
    @property
    def prod_name(self):  # getter for product name
        return str(self.__prod_name).title()

    @prod_name.setter
    def prod_name(self, value):  # setter for product name
        if str(value).isnumeric() == False:
            self.__prod_name == value
        else:
            raise Exception("Names cannot be numbered")

    # Price
    @property
    def price(self):  # getter for price
        return str(self.__price)

    @price.setter  # setter for price
    def price(self, value):
        if value.isnumeric() == True:
            self.__price = value
        else:
            print("Need Enter Number. Not String")

    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class Processor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :return: (list) of objects
        """
        list_of_objects = []
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")

            prod_name = data[0].strip()
            price = float(data[1].strip())
            list_of_objects.append(Product(prod_name, price))

        file.close()
        return list_of_objects

    @staticmethod
    def add_data_to_list(list_of_objects, prod_name, price):
        """Adds data to a list of dictionary row
        :param list_of_objects (list) of objects adding data to it
        :param prod_name: (string) with name of product
        :param price: (string) with price
        """
        list_of_objects.append(Product(prod_name, price))

    @staticmethod
    def remove_data_from_list(list_of_objects, strKeyToRemove):
        """Removes data from a list of dictionary rows
        :param list_of_objects: (list) of objects removing from it
        :param strKeyToRemove: Product to Remove
        :return: Revised list of objects
        """

        sucess_status = False
        prod_number = 0
        for Product in list_of_objects:
            if Product.prod_name == strKeyToRemove:
                del list_of_objects[prod_number]
                sucess_status = True
            prod_number += 1
        return list_of_objects, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_objects):
        f = open(file_name, "w")
        for Product in list_of_objects:
            f.write(str(Product.prod_name + ',' + Product.price + '\n'))
        f.close()
        print("now in file!")
        return list_of_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    #  Print Doc String
    print(Product.__doc__)

    """ Performs Input and Output Products """

    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product 
        2) Remove an existing Product
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        try:  # Error Handling for User Entry
            choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        except ValueError:
            print("Invalid Entry. Please select a valid choice")
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(lstTable):
        """ Shows the current Products in the list of dictionaries rows
        :param lstTable: (list) of objects you want to display
        :return: nothing
        """
        print("******* The Current Products are: *******")
        for Product in lstTable:
            print("Product_Name: {}, Price: {}".format(Product.prod_name, Product.price))
            #print(row["Product_Name"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        """Gets data for a dictionary rows
        :return: (tuple) of string with Products and Price
        """

        prod_name = str(input("What is the product? -")).strip()
        price = input("What is the price? - ").strip()

        print()  # Add an extra line for looks
        return prod_name, price

    @staticmethod
    def input_product_to_remove():
        """Gets a Product from the user to remove
        :return: (string) Product to remove
        """
        prod_name = str(input("What product would you like to remove? - ")).strip()
        return prod_name

# Main Body of Script  ---------------------------------------------------- #
# Step 1 - When the program starts, Load data from ToDoFile.txt.
lstTable = Processor.read_data_from_file(strFileName)  # read file data


# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Products_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Adds a New Products
        tplData = IO.input_new_product_and_price()   # Outputs Tuple with New Product & Priority
        Processor.add_data_to_list(lstTable, tplData[0], tplData[1])   # Adds Data to List
        IO.print_current_Products_in_list(lstTable)
        print("Added New Product Successfully")
        continue  # to show the menu

    elif strChoice == '2':  # Removes an Existing Product
        strKeyToRemove = input("Which Products would you like removed?-")
        blnItemRemoved = Processor.remove_data_from_list(lstTable, strKeyToRemove)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)   # Writes Data to File
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable.clear()
            lstTable = Processor.read_data_from_file(strFileName)   # Outputs List and Sucess
            IO.print_current_Products_in_list(lstTable)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit




