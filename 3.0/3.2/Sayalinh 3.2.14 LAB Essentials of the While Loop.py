blocks = int(input("Enter the number of blocks: "))

height = 0
use_count = 0

while True:
    if height + 1 + use_count <= blocks:
        use_count += height + 1
        height += 1
    else:
        break

print("The height of the pyramid:", height)

# It's mildly annoying that the break keyword skips over the else statement of a loop
#
# do_loop = True
#
# while do_loop:
#     if height + 1 + use_count <= blocks:
#         use_count += height + 1
#         height += 1
#     else:
#        do_loop = False
# else:
#     print("The height of the pyramid:", height)

