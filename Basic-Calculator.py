#בניית פונקציית מחשבון בסיסי שמקבל שני ערכים ומבצע פעולות פשוטות(+,-,/,*)



def calculator(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b != 0:
            return a/b
        else:
            return"Error ,zero can not be divided"
    else:
        return"select legal operation"



while True:
       try:
        a = int(float(input("select first number:")))
        b = int(float(input("select second number:")))
        op = input("select an operation:")

        result = calculator(a,b,op)
        print("result:",result)

       except ValueError:
        print("Invalid input, enter a number")

        again = input("Continue to another order> Y/N:").lower()
        if again != "y":
            print("Thank you for using our service. Goodbye!")
            break
