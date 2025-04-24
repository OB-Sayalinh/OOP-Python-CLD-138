import time

for i in range(5):
    print_string = str(i + 1) + " Mississippi"
    for n in range(13):
        print(print_string[n], end = "")
        time.sleep(1/13)
    print("")

print("Ready or not, here I come!")
