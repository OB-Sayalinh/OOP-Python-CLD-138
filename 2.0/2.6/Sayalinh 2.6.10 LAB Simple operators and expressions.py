x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1/x)))
# Meant to be a flipped equation version of y
y2 = (x + 1 / (x + 1 / (x + 1/x)))

print("y =", y)
print("y flipped =", y2)
print("y multiplied by y flipped =", y2 * y)

