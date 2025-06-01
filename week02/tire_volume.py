import math

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime


def real_number(message):
    real = False
    while not real:
        function_number = input(message)
        try:
            function_number = int(function_number)
            return function_number
        except:
            print("Please put in a whole number.")

use_program = "y"

while use_program[0] == "y":
    tire_width = real_number("\nEnter the width of the tire in mm (ex 205): ")
    tire_aspect = real_number("\nEnter the aspect ratio of the tire (ex 60): ")
    tire_diameter = real_number("\nEnter the diameter fo the wheel in inches (ex 15): ")

    volumn = (math.pi * (tire_width ** 2) * tire_aspect * (tire_width * tire_aspect + 2540 * tire_diameter)) / (10 ** 10)

    print(f"\nThe approximate volume is {volumn:.2f} liters\n")
    
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()
    
    with open("volumes.txt", "at") as f:
        print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {tire_aspect}, {tire_diameter}, {volumn:.2f}", file=f)
    
    use_program = input("Would you like to do another calculation? ")
    
    while use_program == "":
        print("\nPlease enter an answer:")
        use_program = input("Would you like to do another calculation (yes/no)? ")