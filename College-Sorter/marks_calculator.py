def calculate_out_of_800(percentage):
    try:
        percentage = float(percentage)
        if percentage < 0 or percentage > 100:
            return "Please enter a valid percentage between 0 and 100."
        value = (percentage / 100) * 800
        return f"{percentage}% of 800 is {value}"
    except ValueError:
        return "Invalid input. Please enter a number."

while True:
    user_input = input("Enter a percentage (or type 'exit' to quit): ")
    if user_input.lower() in ['exit', 'quit', 'done']:
        print("Exiting the program. Goodbye!")
        break
    result = calculate_out_of_800(user_input)
    print(result)