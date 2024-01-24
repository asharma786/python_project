from formula import radtodeg, degtorad

#degtorad

# Take user input for radians
radians_input = float(input("Enter the angle in radians: "))

# Use the radtodeg function to convert radians to degrees
degrees_result = radtodeg(radians_input)

# Display the result
print(f"{radians_input} radians is equal to {degrees_result:.4f} degrees")

# Take user input for degrees
degrees_input = float(input("Enter the angle in degrees: "))

# Use the degtorad function to convert degrees to radians
radians_result = degtorad(degrees_input)

# Display the result
print(f"{degrees_input} degrees is equal to {radians_result:.4f} radians")
