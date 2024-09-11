def calc_get_number(_current_number):
    #Function used get a number from user
    if _current_number == 0:
        print("Enter Initial Number | Type exit to end calculation")
    else:
        print("Enter Number | Type exit to end calculation")
    value = input()
    if value.isdigit():
        value = int(value)
    elif value.isdecimal():
        value = float(value)
    elif value.lower() == "exit":
        return "exit"
    else:
        print("Error: Please make sure the answer is a Number or exit")
        return "error"
    return value
    
def calc_function():
    """
    Created by Noah Peterson for practice and refreshing on Python
    
    Calculator Function Notes
        At any point a user can type exit to exit function
        Prints an Error if the reponse to a question is wrong
        If for some there is an error with the function it will return a 0 as the result of the calculation
    
    number - Ask for a number
    operator - Ask for one of a few operators +, -, *, x, /, ^
    """
    #Init
    return_value = 0 #Final Value
    calcStep = "number" #Current Step of Calcluator
    _num = 0 #The current number being applied to result
    #Main
    while calcStep != "exit":
        if calcStep == "number": #First Number
            _num = calc_get_number(return_value)
            if _num == "exit":
                calcStep = "exit"
            elif _num != "error":
                if return_value == 0:
                    return_value = _num
                    calcStep = "number"
                else: 
                    calcStep = "operator"
        elif calcStep == "operator":
            print(f'How to apply {_num} to {return_value}')
            print("Enter Operator (+, -, x, /, %, ^, int) | Type back to  | Type exit to end calculation")
            _operator = str(input())
            if _operator == "+" or _operator == "add":
                print(f'{return_value} + {_num} = {return_value + _num}')
                return_value += _num
            elif _operator == "-" or _operator == "sub" or _operator == "subtract":
                print(f'{return_value} - {_num} = {return_value + _num}')
                return_value -= _num
            elif _operator == "*" or _operator == "x" or _operator == "multi" or _operator == "multiply":
                print(f'{return_value} x {_num} = {return_value * _num}')
                return_value *= _num
            elif _operator == "^" or _operator == "pow" or _operator == "power":
                print(f'{return_value} to the power of {_num} = {pow(return_value, _num)}')
                return_value = pow(return_value, _num)
            elif _operator == "/" or _operator == "divide":
                if _num == 0:
                    print("Error : Cannot divide a number by 0. Please choose another operator or type back / exit")
                    continue
                print(f'{return_value} / {_num} = {return_value / _num}')
                return_value /= _num
            elif _operator == "%":
                if _num == 0:
                    print("Error : Cannot modulo a number by 0. Please choose another operator or type back / exit")
                    continue
                print(f'{return_value} mod {_num} = {return_value % _num}')
                return_value %= _num
            elif _operator == "back":    
                calcStep = "number"
                _num = 0
            elif _operator == "exit":  
                calcStep = "exit"
                continue
            else:
                print("Error: Please enter one of the listed Operators.")
                continue
            calcStep = "number"
            _num = 0
        else: 
            print("An error as occurred. Please make sure to answer steps with the correct response.")
            print("Calcluator will return 0")
            return_value = 0
            calcStep = "exit"
    print("Exiting Calcluator")   
    #Returns an Int or Float
    if isinstance(return_value, (int, float)):
        return return_value
    else:
        return 0

print("Final Result: " + str(calc_function()))    
