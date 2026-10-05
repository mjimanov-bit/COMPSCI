reminders = []
current_reminder = 0


def update_screen():
    if len(reminders) == 0:
        print("No reminders yet.")
    else:
        print(str(current_reminder + 1) + " / " + str(len(reminders)))
        print(reminders[current_reminder])


while True:
    print("\n1. Previous")
    print("2. Next")
    print("3. Add reminder")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        if current_reminder > 0:
            current_reminder -= 1
        update_screen()

    elif choice == "2":
        if current_reminder < len(reminders) - 1:
            current_reminder += 1
        update_screen()

    elif choice == "3":
        reminder = input("Enter a reminder: ")
        reminders.append(reminder)
        current_reminder = len(reminders) - 1
        update_screen()

    elif choice == "4":
        break
