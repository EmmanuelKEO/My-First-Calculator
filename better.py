OPERATORS:list = ['/', '*', '-', '+', '(', ')']
NUMBERS:list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
ALPHABETS:list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def calculate(expression:str) -> float:
    expression = '+' + expression
    expression = expression + '+'
    process:list = []
    process1:list = []
    process2:list = []
    process3:list = []
    process4:list = []
    sign:int = 1
    number:str = ''
    prevoius_item:str = ''
    result:float = 0
    b1:int = 0
    b2:int = 0
    catch:bool = False

    for current_item in expression:
        if current_item in ALPHABETS:
            while True:
                print(current_item + '?')
                response:str = input('>>')
                if response in NUMBERS:
                    if prevoius_item in NUMBERS:
                        process.append('*')
                    process.append(response)
                    break
                else:
                    print(response, 'is not a number.')
        else:
            process.append(current_item)
        prevoius_item = current_item
   
    for current_item in process:
        if current_item in OPERATORS + ['#']:
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
            b1 = b1 + 1
        if current_item == ')':
            b2 = b1
            b1 = b1 - 1
        if b2 == 1:
            catch = False
            b1 = 0
            b2 = 0
        if catch:
            number = number + str(current_item)
        else:
            if number == '':
                if not current_item in ['(', ')']:
                    process2.append(current_item)
            else:
                process2.append('*')
                process2.append(calculate(number))
                number = ''
        if b1 == 1:
            catch = True
    number = ''
    for current_item in process2:
        if current_item in ['*', '/', '#']:
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
        if current_item in ['*', '#']:
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
    for current_item in process4:
        if not current_item == '#':
           result = result + current_item
    return result

def is_valid(expression:str) -> bool:
    VALID:list = NUMBERS + OPERATORS + ALPHABETS + [' ']
    for item in expression:
        if not item in VALID:
            return False
    return True

def main() -> None:
    print('Basic calculator')
    response:str = ''
    while True:
        response = input('>')
        if response.upper() in ['HELP','?']:
            print('This is a basic calculator that supports the following operations: + - / * ()')
        elif response.upper() in ['EXIT','END','QUIT','CLOSE']:
            input('press any key to quit.')
            break
        elif is_valid(response):
            print(calculate(response))
        else:
            print('invalid input')

if __name__ == '__main__':
    main()