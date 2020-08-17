def operate(num1, num2, sign):

    if sign == "+":
        return float(num1 + num2)
    elif sign == "-":
        return float(num1 - num2)
    elif sign == "*":
        return float(num1 * num2)
    elif sign == "/":
        return float(num1 / num2)
    else:
        "Invalid choice"

def main():
    '''
    1. Ask user to input one number, convert to inf/float, save it as num1
    2. Ask user to input another number, convert to inf/float, save it as num2
    3. Ask user for math operator [+, -, *, /] keep it simple for now, save it as sign
    5. We have already written function operate(num1, num2, sign), so don't worry about that
    ***operate(num1, num2, sign) returns a float assigned to the variable result 
       the answer as "The answer is" + str(result) with the helo pf string concatenation
    '''
    # Write your code here

    result = operate(num1, num2, sign)
    return 0

if __name__ == "__main__":main()

    
    
    