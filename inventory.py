from tabulate import tabulate


# ========The beginning of the class==========


# Shoe class with country, code, product, cost and quantity attributes.
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)  # Convert cost to float
        self.quantity = int(quantity)  # Convert quantity to integer

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    # String representation of the Shoe object for easy printing
    def __str__(self):
        return (
            f"Country: {self.country}, "
            f"Code: {self.code}, "
            f"Product: {self.product}, "
            f"Cost: {self.cost}, "
            f"Quantity: {self.quantity}"
        )


# =============Shoe list===========

shoe_list = []


# ==========Functions outside the class==============


# Function to read shoe data from the inventory.txt file and populate shoe_list
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line
            for line in file:
                line = line.strip()
                if line:  # Check if the line is not empty
                    temp = line.split(",")
                    shoe = Shoe(temp[0], temp[1], temp[2], temp[3], temp[4])
                    shoe_list.append(shoe)
    # Handle the case where the file does not exist
    except FileNotFoundError:
        print("File not found.")
    # Handle any other exceptions that may occur
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to capture shoe data from user input and add it to shoe_list
def capture_shoes():
    new_shoe = Shoe(
        input("Enter the country: "),
        input("Enter the code: "),
        input("Enter the product: "),
        input("Enter the cost: "),
        input("Enter the quantity: "),
    )
    shoe_list.append(new_shoe)


# Function to view all shoes in the inventory in a tabular format
def view_all():
    if not shoe_list:  # Check if shoe_list is empty
        print("No shoes in inventory.")
        return
    shoe_data = [
        [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        for shoe in shoe_list
    ]

    # Print the shoe data in a tabular format using the tabulate library
    print(
        tabulate(
            shoe_data,
            headers=["Country", "Code", "Product", "Cost", "Quantity"],
            tablefmt="grid",
        )
    )


# Function to find the shoe with the lowest quantity and offer to restock it
def re_stock():
    shoe_list.sort(
        key=lambda x: x.quantity
    )  # Sort shoe_list in ascending orde
    lowest_shoe = shoe_list[0]
    print(f"The shoe with the lowest quantity is: {lowest_shoe}")
    add_quantity = input(
        "Do you want to add quantity to this shoe? (yes/no): "
    )
    if add_quantity.lower() == "yes":  # Check if user wants to add quantity
        # Try to convert user input to an integer and update the shoe quantity
        try:
            additional_quantity = int(input("Enter the quantity to add: "))
            lowest_shoe.quantity += additional_quantity
            print(
                f"Updated shoe: {lowest_shoe}"
            )  # Print the updated shoe info
        # Handle the case where the user input is not a valid integer
        except ValueError:
            print("Invalid input. Quantity must be an integer.")
        update_file()


# Function to update the inventory.txt file with the current shoe_list data
def update_file():
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for s in shoe_list:
            file.write(
                f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n"
            )


# Function to search for a shoe by its code and display its details
def search_shoe():
    search_code = input("Enter the shoe code to search: ").strip().lower()
    found = False
    for shoe in shoe_list:
        if shoe.code.lower() == search_code:
            print(shoe)
            found = True
    # If no shoe is found with the given code, print a message
    if not found:
        print("Shoe not found.")


# Function to calculate and display the total value of each shoe
def value_per_item():
    if not shoe_list:
        print("No shoes available.")
        return

    # Create a table of shoe products and their total value (cost * quantity)
    table = []

    # Calculate the total value for each shoe and add it to the table
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        table.append([shoe.product, f"R{value:.2f}"])

    print(tabulate(table, headers=["Product", "Value"], tablefmt="grid"))


# Function to find and display the shoe with the highest quantity for sale
def highest_qty():
    shoe_list.sort(key=lambda x: x.quantity)
    highest_shoe = shoe_list[-1]
    print(f"Shoe for sale: {highest_shoe}")


# TESTING get_cost and get_quantity
test_shoe = Shoe("SA", "SA01", "Air Max", 1200, 50)
print("Cost:", test_shoe.get_cost())
print("Quantity:", test_shoe.get_quantity())


# ==========Main Menu=============
def main_menu():
    read_shoes_data()  # Load data from file at the start of the program
    # Main menu to interact with the user
    while True:
        print("\nShoe Inventory Management System")
        print("1. Read shoe data from file")
        print("2. Capture new shoe")
        print("3. View all shoes")
        print("4. Restock shoe with lowest quantity")
        print("5. Search for a shoe by code")
        print("6. Calculate value per item")
        print("7. Display shoe with highest quantity for sale")
        print("8. Exit")

        # Get user input for menu choice and handle the corresponding action
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
            update_file()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting the program.")
            break
        # Handle invalid menu choices
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# Run the main menu when the script is executed
if __name__ == "__main__":
    main_menu()
