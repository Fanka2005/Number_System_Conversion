import Conversion_Mechanism as cm

def console_dropdown(options_list, prompt_message):
    print(prompt_message)
    for index, option in enumerate(options_list, 1):
        print(f"{index}. {option}")
    
    while True:
        try:
            choice_index = int(input("Enter the number of your choice: "))
            if 1 <= choice_index <= len(options_list):
                return options_list[choice_index - 1]
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


numbers = str(input("Input your number: "))
conversion = ["Binary to Decimal", "Decimal to Binary", "Binary to Hexadecimal", "Hexadecimal to Binary", "Decimal to Hexadecimal", "Hexadecimal to Decimal"]
selected_conversion = console_dropdown(conversion, "Please select your conversion: ")

match selected_conversion:
    case "Binary to Decimal":
        print(cm.Binary_Decimal(numbers))
    case "Decimal to Binary":
        print(cm.Decimal_Binary(numbers))
    case "Binary to Hexadecimal":
        print(cm.Binary_Hexadecimal(numbers))
    case "Hexadecimal to Binary":
        print(cm.Hexadecimal_Binary(numbers))
    case "Decimal to Hexadecimal":
        print(cm.Decimal_Hexadecimal(numbers))
    case "Hexadecimal to Decimal":
        print(cm.Hexadecimal_Decimal(numbers))
    


