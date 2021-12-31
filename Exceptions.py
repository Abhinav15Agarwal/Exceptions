# Exceptions - They are used the programmer doesn't want the code to crash but if failed
# give a suitable output so that the user knows the program crashed

try:
    age = int(input("age- "))
    print(age)
except ValueError:
    print("Invalid Input")