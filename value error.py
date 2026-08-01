try:
    number = int(input("enter a number: "))
    print(" the number is printed", number)

except ValueError as ex:
  print ("Exeption", ex)