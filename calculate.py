while True:
    print("calculator")

    num1 = float(input("Enter a number"))
    operator = input("enter a operator(+,-,*,/)")
    num2 = float (input("Enter a number"))

    if operator == ("+"):
        print("result:", num1+num2)

    elif operator == ("-"):
       print("result:", num1-num2)

    elif operator == ("*"):
     print("result:", num1*num2)

    elif operator == ("/"):
      if num2!= 0:
       print("result:", num1/num2)
    else:
       print("cannot divide by 0")
else:
     print("invalid operation")   
   

      
