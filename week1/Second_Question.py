'''
Name: Astha Sharma
Class:Question 2 Answer
THe below program has been solved on very basic level where the program will not exit untill the user inputs the no

'''





def troubleshoot_diesel_engine():
    while True:
        check_status_light()

        run_again = input("Do you want to run the test again? (yes/no): ").strip().lower()
        if run_again != "yes":
            break

def check_status_light():
    color = input("Enter the color of the status lights (Red/Green/Amber): ").strip().lower()

    if color == "red":
        handle_red_light()
    elif color == "green":
        do_restart_procedure()
    elif color == "amber":
        check_fuel_line_service()
    else:
        print("Invalid color. Please enter Red, Green, or Amber.")

def handle_red_light():
    try:
        print("Shut-off all input lines and check meter #3")
        meter_reading = float(input("Enter meter #3 reading: "))
        
        if meter_reading < 50:
            check_main_line_pressure()
        elif meter_reading >= 50:
            measure_flow_velocity()
        else:
            print("Invalid reading. Please enter a valid meter reading.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def check_main_line_pressure():
    pressure = input("Is the main line pressure High, Low, or Normal? ").strip().lower()
    
    if pressure == "normal":
        refer_to_motor_service_manual()
    elif pressure in ["high", "low"]:
        refer_to_main_line_manual()
    else:
        print("Invalid input. Please enter High, Low, or Normal.")

def measure_flow_velocity():
    velocity = input("Enter the flow velocity at inlet 2-B (High/Low/Normal): ").strip().lower()
    
    if velocity == "normal":
        refer_to_inlet_service_manual()
    elif velocity in ["high", "low"]:
        refer_unit_for_factory_service()
    else:
        print("Invalid input. Please enter High, Low, or Normal.")

def do_restart_procedure():
    print("Performing restart procedure")

    # Add additional steps as needed

def check_fuel_line_service():
    print("Checking fuel line service routine...")
    # Add additional steps as needed

def refer_to_motor_service_manual():
    print("Please refer to the motor service manual.")

def refer_to_main_line_manual():
    print("Please refer to the main line manual.")

def refer_to_inlet_service_manual():
    print("Please refer to the inlet service manual.")

def refer_unit_for_factory_service():
    print("Please refer the unit for factory service.")

if __name__ == "__main__":
    troubleshoot_diesel_engine()
