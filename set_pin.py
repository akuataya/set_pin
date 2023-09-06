pin_set = False

while pin_set == False:
    pin = input("Set a new PIN (4 numbers): ")

    if len(pin) != 4 or not pin.isdigit():
        print("Please enter 4 numbers.")

    else:
        pin_set = True
        print("Your new PIN is: " + pin)
