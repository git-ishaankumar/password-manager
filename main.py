import sys

print("\n🔑 Welcome to Password Manager!\n")
hide = False
ophide = "Hide"


def choose():
    global ophide
    option = input(
        f"**********************\n\n1️⃣ Add New Account\n2️⃣ View All Accounts\n3️⃣ Find Specific Password\n4️⃣ {ophide} Passwords\n5️⃣ Quit\n\n**********************\n\n"
    )
    if option not in ["1", "2", "3", "4", "5"]:
        print("\nPlease enter either 1, 2, 3, 4, or 5\n")
        return choose()
    else:
        return option


apps = []
usernames = []
passwords = []
accountnum = 0


def new():
    def addapp():
        app = input("\nPlease enter the application this account will be for:\n")
        if app.strip() == "":
            print("\nPlease enter a value.\n")
            return addapp()
        else:
            apps.append(app)

    def unames():
        uname = input("\nPlease enter the username for this application:\n")
        if uname.strip() == "":
            print("\nPlease enter a value.\n")
            return unames()
        else:
            usernames.append(uname)

    def pwords():
        pword = input("\nPlease enter the password for this application:\n")
        if pword.strip() == "":
            print("\nPlease enter a value.\n")
            return pwords()
        else:
            passwords.append(pword)

    addapp()
    unames()
    pwords()
    print("\nAdding details...\n")
    print("Success! ✅\n")
    global accountnum
    accountnum += 1


def view():
    global accountnum
    global hide
    print(
        f"\n**********************\nAll {accountnum} Accounts:\n**********************"
    )
    for i in range(accountnum):
        if hide:
            password_display = "*" * len(passwords[i])
        else:
            password_display = passwords[i]
        print(f"{apps[i]} | Username: {usernames[i]} | Password: {password_display}")


def specific():
    global apps
    global usernames
    global passwords
    global hide
    specific_app = input("\nPlease enter a specific application to see its details:\n")
    if specific_app not in apps:
        print("\nPlease enter an account you have entered into the manager.")
        return specific()
    else:
        index = apps.index(specific_app)
        if hide:
            password_display = "*" * len(passwords[index])
        else:
            password_display = passwords[index]
        print(
            f"\n**********************\n{apps[index]} | Username: {usernames[index]} | Password: {password_display}\n"
        )


quit = False


while not quit:
    choice = choose()
    if choice == "1":
        new()
    elif choice == "5":
        quit = True
    elif choice == "4":
        hide = not hide
        if hide:
            ophide = "Show"
        else:
            ophide = "Hide"
    elif choice == "2":
        view()
    elif choice == "3":
        specific()

print("\nThank you for using Password Manager! 👋")
sys.exit()
