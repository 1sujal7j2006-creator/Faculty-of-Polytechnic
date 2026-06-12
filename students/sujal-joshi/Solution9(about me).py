def about_me():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    language = input("Enter your favourite programming language: ")
    years = int(input("How many years have you been coding? "))

    print("\n--- About Me ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Favourite Programming Language: {language}")
    print(f"Years of Coding Experience: {years}")
    print("----------------")

about_me()
