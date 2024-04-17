def is_valid(_expression):
    Valid_list = ['/','*','-','+','1','2','3','4','5','6','7','8','9','0','.',' ','(',')']
    for _item in _expression:
        if not _item in Valid_list:
            return False
    return True

def operate(value1, operator, value2):
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2

def get_list_size(_list):
    count = 0
    for x in _list:
        count += 1
    return count
def calculate(_expression, _show):
    Sign = 1
    Number = '0'
    New_expression = []
    _expression = _expression + '+'
    for _current_item in _expression:
        if _current_item in ['/','*','-','+','(',')']:
            if not Number == '0':
                New_expression.append(float(Number) * Sign)
                Number = '0'
                Sign = 1  
                if _current_item in ['-','+']:
                    New_expression.append('#')

                if _current_item in ['/','*','(',')']:
                    New_expression.append(_current_item)
            else:
                if _current_item == '(':
                    New_expression.append(1)
                    Number = '0'
                    Sign = 1  
                    if _current_item in ['-','+']:
                        New_expression.append('#')

                    if _current_item in ['/','*','(',')']:
                        New_expression.append(_current_item)
        else:
            Number = Number + _current_item

        if _current_item == '+':
            Sign = 1

        if _current_item == '-':
            Sign = -1

    Result = 0.0
    Last_number = 0.0
    Operator = '#'
    Bracket_stack = []
    Product_switch = 0
    Sum = 0.0
    Product = 0.0
    Bracket_switch = 0
    for _current_item in New_expression:
        if _current_item in ['*','/','(',')','#']:
            Operator = _current_item
        if Operator in ['*','/'] and not _current_item in ['*','/']:
            Product_switch += 1
            if Product_switch == 1:
                Sum = Sum - Last_number
                Product = operate(Last_number,Operator,_current_item)
            if Product_switch > 1:
                Product = operate(Product,Operator,_current_item)

            Operator = '#'
            Last_number = Result

        if not _current_item in ['*','/','(',')','#']:
            Last_number = _current_item
            if Operator == '#':
                if Product_switch == 0:
                    Sum = Sum + _current_item

        if _current_item == '#':
            Sum = Sum + Product
            Product_switch = 0
            Product = 0.0

        if Operator in ['('] and _current_item in ['(']:
            Bracket_switch += 1
            Sum = Sum - Last_number
            Bracket_stack.append(Last_number)
            if Bracket_switch == 1:
                Result = Sum
                Sum = 0.0
            Operator = '#'
            Bracket_switch += 1
        if Operator in [')'] and _current_item in [')']:
            Sum = Sum + Product
            Product = 0.0
            Product_switch = 0
            if get_list_size(Bracket_stack) == 1:
                Result = Result + Sum * Bracket_stack.pop()
                Sum = Result
                Result = 0.0
                Bracket_switch = 0
            else:
                Sum = Sum * Bracket_stack.pop()
            Last_number = Sum
            Operator = '#'

        
        if _show:
            print('expression:',New_expression)
            print('Result:',Result)
            print('Last_number:',Last_number)
            print('Operator:',Operator)
            print('Bracket_stack:',Bracket_stack)
            print('Product_switch:',Product_switch)
            print('Sum:',Sum)
            print('Product:',Product)
            print('Bracket_switch:',Bracket_switch)
            print('_current_item:',_current_item)
            input('continue?')
            print(" ")
            
        
    return Sum

def main():
    print('Calculator')
    response = ''
    debug_mode = False
    current_problem = '3+2(2(2*4+5)(6+8))+5'
    while True:
        response = input('> ')
        if response.upper() in ['EXIT','CLOSE','END','QUIT']:
            break
        elif response.upper() in ['HELP']:
            print('Type exit, close, end or quit to close pycalc')
        elif response.upper() in ['DEBUG']:
            print('debug mode toggled')
            debug_mode = (debug_mode + 1) % 2
        elif is_valid(response):
            print(calculate(response,debug_mode))
            #print(eval(response))
            
        else:
            print('Invalid input')

if __name__ == "__main__":
    main()
