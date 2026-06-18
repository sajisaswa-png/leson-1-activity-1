string = input("enter your own word :")
char = input("enter your own charecter :")
i = 0
count = 0
while(i <len(string)) :

    if (string[i] == char):
        count = count +1
    i = i + 1
print("the total number of times", char , "has occored =",count)