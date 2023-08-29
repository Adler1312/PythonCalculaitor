def plus(x, y):
    return x+y
def minus(x, y):
    return x-y
def mal(x, y):
    return x*y
def geteiltdurch(x, y):
    return x/y
def main():
    print("Wähle die Zeichen")
    print("1. + ")
    print("2. - ")
    print("3. * ")
    print("4. / ")

    choice = int(input("Wähle zwischen (1/2/3/4): "))
    num1 = int(input("Gib deine erste Zahl ein: "))
    num2 = int(input("Gib deine zweite Zahl ein: "))

    if choice == 1:
        print(f"Das Ergebnis lautet {num1} + {num2} = {plus(num1, num2)}")
    if choice == 2:
        print(f"Das Ergebnis lautet {num1} - {num2} = {minus(num1, num2)}")
    if choice == 3:
        print(f"Das Ergebnis lautet {num1} * {num2} = {mal(num1, num2)}")
    if choice == 4:
        print(f"Das Ergebnis lautet {num1} / {num2} = {geteiltdurch(num1, num2)}")
    else:
        print("Ungültige eingabe")
main()