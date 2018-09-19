def question():
    user_input = input("What is your question?: ")
    while user_input[-1] != "?":
        print("I'm sorry, I can only answer questions.")
        user_input = input("What is your question?: ")
    return user_input

first_pass = question()
