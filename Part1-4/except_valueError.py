try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)

except( ZeroDivisionError ):
    print("Invalid input.")
except( ValueError ):
    print("It's not value !")