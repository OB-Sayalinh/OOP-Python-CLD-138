def check_is_number(num):
    try:
        float(num)
        return True
    except:
        return False

# Loops through inputs for a type correct float from the input
def loop_for_number():
    final_input = None
    given = input("Please enter a number: ")
    while True:
        if check_is_number(given):
            final_input = float(given)
            break
        else:
            given = input("Sorry, the input given was not a number: ")
    return final_input


num1 = loop_for_number()
num2 = loop_for_number()

print("The numbers added up =", num1 + num2)
print("The numbers subtracted =",num1 - num2)
print("The numbers multiplied =", num1 * num2)
print("The numbers divided =", num1 / num2)

print("Thanks for your time!")