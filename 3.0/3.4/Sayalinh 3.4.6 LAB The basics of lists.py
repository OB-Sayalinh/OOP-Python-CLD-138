hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

user_number = int(input("Please enter a number: "))
hat_list[2] = user_number

del hat_list[-1]

print(len(hat_list))

print(hat_list)

# Flipping a list

# No pointers, yet if you were to just declare this without copy it retains the changes to hat_list
copy_hat_list = hat_list.copy()

for n in range(len(hat_list)):
    hat_list[n] = copy_hat_list[-n - 1]

print(hat_list)