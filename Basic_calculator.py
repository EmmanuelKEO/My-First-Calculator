def calculate(expression:str):
    sign:int = 1
    number:str = ''
    expression = '+' + expression
    expression = expression + '+'
    process:list = []
    process1:list = []
    process2:list = []
    process3:list = []
    process4:list = []
    B1:int = 0
    B2:int = 0
    catch:bool = False
    last_operator:str = ''
    result:float = 0
    prevoius_item = ''
    if is_equation(expression) == 0:
        for current_item in expression:
            if is_alphabet(current_item):
                while True:
                    print(current_item + '?')
                    res = input('>')
                    if is_number(res):
                        if is_number(prevoius_item):
                            process.append('*')
                        process.append(res)
                        break
                    else:
                        print(res,'is not a number.')
            else:
                process.append(current_item)
            prevoius_item = current_item
   
    for current_item in process:
        if current_item in ['+','-','(',')','*','/','#']:
            if number == '' and current_item == '(':
                number = '1.0'

            if not number == '':
                process1.append(float(number) * sign)
                number = ''
                sign = 1

            if current_item in ['(',')','*','/','#']:
                process1.append(current_item)
            else:
                process1.append('#')

        else:
            number = number + current_item

        if current_item == '+':
            sign = 1

        if current_item == '-':
            sign = -1
    number = ''
    for current_item in process1:
        if current_item == '(':
            B1 = B1 + 1
        if current_item == ')':
            B2 = B1
            B1 = B1 - 1
        if B2 == 1:
            catch = False
            B1 = 0
            B2 = 0
        if catch:
            number = number + str(current_item)
        else:
            if number == '':
                if not current_item in ['(',')']:
                    process2.append(current_item)
            else:
                process2.append('*')
                process2.append(calculate(number))
                number = ''
        if B1 == 1:
            catch = True
    number = ''
    for current_item in process2:
        if current_item in ['*','/','#']:
            if not current_item == '/':
                if number == '':
                    process3.append(current_item)
                else:
                    process3.append(float(number))
                    process3.append(current_item)
                number = ''
        else:
            if number == '':
                number = current_item
            else:
                number = str(float(number) / float(current_item))   
    number = ''
    for current_item in process3:
        if current_item in ['*','#']:
            if not current_item == '*':
                if number == '':
                    process4.append(current_item)
                else:
                    process4.append(float(number))
                    process4.append(current_item)
                number = ''
        else:
            if number == '':
                number = current_item
            else:
                number = str(float(number) * float(current_item))
    number = ''
    for current_item in process4:
        if not current_item == '#':
           result = result + current_item
    return result

def is_valid(data:str):
    valid:list = ['1','2','3','4','5','6','7','8','9','0','-','+','*','/','.','(',')',' ','=']
    for item in data:
        if not item in valid:
            if not is_alphabet(item):
                return False
    if is_equation(data) > 1:
        return False
    return True

def is_equation(data:str):
    count = 0
    for item in data:
        if item == '=':
            count += 1
    return count

def is_operator(data:str):
    for item in data:
        if not item in ['/','*','-','+','(',')']:
            return False
    return True

def is_number(data:str):
    for item in data:
        if not item in ['1','2','3','4','5','6','7','8','9','0','.']:
            return False
    return True

def is_alphabet(data:str):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for item in data:
        if not item in alphabet:
            return False
    return True

def main():
    print('Basic calculator')
    response:str = ''
    while True:
        response = input('>')
        if response.upper() in ['HELP','?']:
            print('This is a basic calculator that supports the following operations: + - / * ()')
        elif  '=' in response:
            print('"=" is not supported!')
        elif response.upper() in ['EXIT','END','QUIT','CLOSE']:
            input('press enter to quit.')
            break
        elif is_valid(response):
            print(calculate(response))
        else:
            print('invalid input')

if __name__ == '__main__':
    main()