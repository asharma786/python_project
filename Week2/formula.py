import math

def radtodeg(radians):
    degrees = radians * (180 / math.pi)
    return degrees

def degtorad(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# retail Q2 here

def get_wholesale_cost():
    wholesale = float(input("Enter the item's wholesale cost: "))
    
    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost: '))
    
    return wholesale

def calculate_retail_price(wholesale, mark_up=2.5):
    retail = wholesale * mark_up
    return retail
