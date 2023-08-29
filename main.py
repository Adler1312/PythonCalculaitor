def plus(x, y):
    return x+y


def main():
    num1 = int(input("Gib deine erste Zahl ein"))
    num2 = int(input("Gib deine zweite Zahl ein"))

    print(f"Das Ergebnis lautet {num1} + {num2} = {plus(num1, num2)}")

main()