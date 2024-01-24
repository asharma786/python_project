# W2_Q2.py
#Here the program is written  to calculate the retail prices and wholesale prices
#I tried to explore main finction but it has not much impact on program except it helps in debugging and execution but i read it hence wanted to utilize this
#uncommenting for now

#Use which i read of main section
# The if __name__ == "__main__": block helps you avoid unintended execution of this code when the script is imported

from formula import get_wholesale_cost, calculate_retail_price

def main():
    mark_up = 2.5  # The markup percentage
    another = 'y'  # Variable to control the loop.

    # Process one or more items.
    while another == 'y' or another == 'Y':
        # Get the item's wholesale cost.
        wholesale = get_wholesale_cost()

        # Calculate  retail price.
        retail = calculate_retail_price(wholesale)

        # Display the retail price.
        print('Retail price: $', format(retail, ',.2f'))

        # Do this again?
        another = input('Do you have another item? (Enter y for yes): ')

if __name__ == "__main__":
 main()
