def Decimal_Binary(input: str)->str:
    input = int(input)
    binary = []
    if input >= 0 and input <= 1:
        return str(input)
    while input > 1:
        input_truncated = input//2
        input_rm = input%2
        binary.append(input_rm)
        if input_truncated == 1:
            binary.append(1)
            binary.reverse()
            placeholder_binary = ''
            for i in binary:
                placeholder_binary += str(i)
            binary = placeholder_binary
            return binary
        input = input_truncated

    return None

def Binary_Decimal(input: str)->int:
    input_list = list(map(int, input))
    input_list.reverse()
    decimal = 0
    for index, i in enumerate(input_list):
        decimal += i*(2**index)
    
    return decimal

def Decimal_Hexadecimal(input: str)->str:
    input = int(input)
    hexadecimal = []
    hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    if (input >= 0) and (input <= 9):
        return str(input)
    elif (input > 9) and (input <= 15):
        return str(hex_dict[input])
    
    while input > 15:
        input_truncated = input//16
        input_rm = input%16
        if (input_rm > 9) and (input <= 15):
            hexadecimal.append(hex_dict[input_rm])
        else :
            hexadecimal.append(input_rm)

        if input_truncated <= 15:
            hexadecimal.append(input_truncated)
            hexadecimal.reverse()
            placeholder_hexadecimal = ''
            for i in hexadecimal:
                placeholder_hexadecimal += str(i)
            hexadecimal = placeholder_hexadecimal
            return hexadecimal
        input = input_truncated
    return None

def Hexadecimal_Decimal(input: str)->int:
    input_list = list(input)
    input_list.reverse()
    decimal = 0
    hex_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for index, i in enumerate(input_list):
        
        try:
            decimal += int(i)*(16**index)
        except:
            i_int = hex_dict[i]
            decimal += i_int*(16**index)

    return decimal

def Binary_Hexadecimal(input: str)->str:
    hexadecimal = Decimal_Hexadecimal(str(Binary_Decimal(input)))
    
    return str(hexadecimal)

def Hexadecimal_Binary(input: str)->str:
    binary = Decimal_Binary(str(Hexadecimal_Decimal(input)))

    return binary
