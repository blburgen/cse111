"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
use_calculator = "y"

while use_calculator.lower()[0] == "y":
    correct_input = False

    while not correct_input:
        age = input("\nPlease enter your age: ")
        try:
            age = int(age)
            correct_input = True
        except:
            print("That is not a whole number")
            
    print(f"\nWhen you exercise to strengthen your heart, you should")
    print(f"keep your heart rate between {(220 - age) * .65:.0f} and {(220 -age) * .85:.0f} beats per minute.\n")
    
    use_calculator = input("Would you like to calculate a different age (yes/no)?")
    
    while use_calculator == "":
        print("\nPlease input an answer.")
        use_calculator = input("Would you like to calculate a different age (yes/no)?")