# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week)
day_of_week = 3
discount = 0

subtotal = float(input("Please enter the subtotal: "))

if (day_of_week == 2 or day_of_week == 3):
    if subtotal >= 50:
        discount = round(0.1 * subtotal, 2)
        print(f"Discount amount: {discount}")
    else:
        print(f"You need ${50 - subtotal:.2f} more to receive a discount today.")
    
sale_tax = round((subtotal - discount) * 0.06, 2)

print(f"Sales tax amount: {sale_tax}")
print(f"Total: {subtotal - discount + sale_tax:.2f}")