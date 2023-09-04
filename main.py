import sys

from actions import add_url, remove_url, fetch_data

while True:
    print("""What would you like to do?
    (0) Exit
    (1) Add an URL
    (2) Remove an URL
    (3) Fetch data""")

    action = input("> ").strip()

    if action == "0":
        sys.exit(0)

    elif action == "1":
        print()
        add_url()

    elif action == "2":
        print()
        remove_url()

    elif action == "3":
        print()
        fetch_data()

    else:
        print("Please enter a valid number.\n")
