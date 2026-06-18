def ask_yes_no(question):
    while True:
        answer = input(question).strip()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print('Please type "y" or "n".')

result = ask_yes_no("Do you like Python? (y/n): ")
print(result)
