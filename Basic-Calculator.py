#בניית פונקציית מחשבון בסיסי שמקבל שני ערכים ומבצע פעולות פשוטות(+,-,/,*)

#a = int(input("select first number:"))
#b = int(input("select second number:"))
#op = input("select an operation")

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


#print(calculator(a,b,op))

#אחרי כל פעולת חישוב שמסתיימת בהצלחה יקפוץ למשתמש שיצטרך לענות עליה ובהתאם לכך תיקבע התנהגות התוכנית
#אני מוודא גם שהמשתמש יכניס קלט נכון (מספר בלבד,כל הזנה אחרת תיחשב לקלט שגוי)

while True:
       try:
        a = int(float(input("select first number:")))
        b = int(float(input("select second number:")))
        op = input("select an operation:")

        result = calculator(a,b,op)
        print("result:",result)

        Continue = input("continue to another order? Y/N: ")

        Continue = Continue.lower()

        if Continue == "y":
            a = int(float(input("select first number:")))
            b = int(float(input("select second number:")))
            op = input("select an operation:")

            result = calculator(a, b, op)

            print("result:",result)

            Continue = input("continue to another order? Y/N: ")

            Continue = Continue.lower()

        else:
            print("Thank you for using our service")
            break

#כאן מכסים את האופציה לקלט שגוי מצד המשתמש עם אופציה להזדמנות נוספת להזנת קלט נכון
       except:
        print("'invalid input' enter a number")

        again = input("Do you want to run another calculation? (yes/no:")

        again = again.lower()

        if again != "yes":
           print("Goodbye")
           break














