def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a Number: "))

            if response < low:
                print("Too Cold!!")
            else:
                return response

        except ValueError:
            print("Please enter a number")

NUMBER = temp_check(-273)
print("you chose {}".format(number))


