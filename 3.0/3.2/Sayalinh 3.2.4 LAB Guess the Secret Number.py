secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

n = int(input("[Integer]: "))

while n != secret_number:
    print("""
+================================+
| HA! HA! HA! HA! HA!            |
| You're stuck in my loop!       |
+================================+
    """)

    n = int(input("[Integer]: "))

print("""
+================================+
| Well done, muggle!             |
| You are free now.              |
+================================+
""")