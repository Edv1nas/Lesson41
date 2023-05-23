from refactored_app import choose_login, choose_to_register_user, choose_create_new_task, chooose_to_update_task, choose_to_show_user_task, choose_to_delete_task


print("Welcome to your TODO application!")
while True:
    choice = input(
        "Please choose an option from the list:\n1. Log in\n2. Register\n3. Exit\n")
    if choice == "1":
        user = choose_login()
        if user:
            print(f"Welcome, {user.username}!")
            while True:
                task_choice = input(
                    "Please choose an option from the list:\n1. Add task\n2. Update task\n3. Show tasks\n4. Delete task\n5. Log out\n")

                if task_choice == "1":
                    choose_create_new_task(user)

                elif task_choice == "2":
                    chooose_to_update_task(user)

                elif task_choice == "3":
                    choose_to_show_user_task(user)

                elif task_choice == "4":
                    choose_to_delete_task(user)

                elif task_choice == "5":
                    break

    elif choice == "2":
        choose_to_register_user()

    elif choice == "3":
        print("Have a great day!")
        break
    else:
        print("Invalid choice.")
