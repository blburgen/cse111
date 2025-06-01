import math

def real_number(message):
    real = False
    while not real:
        return_number = input(message)
        try:
            return_number = int(return_number)
            return return_number
        except:
            print("Please enter a whole number")

number_items = real_number("Enter the number of items: ")
items_box = real_number("Enter the number of items per box: ")

print(f"For {number_items} items, packing {items_box} items in each box, you will need {math.ceil(number_items / items_box)} boxes.")