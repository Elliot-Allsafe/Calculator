import sys


def run():
    print("Valid Operators are :> + - * / %")
    try:
        f_n = int(input("Enter First Number:> "))
        s_n = int(input("Enter Second Number:> "))
        op = str(input("Enter the Operation:> "))
        if op == '+':
            print("> "+str(f_n + s_n))
        elif op == '-':
            if f_n > s_n:
                print("> "+str(f_n - s_n))
            else:
                print("> "+str(s_n - f_n))
        elif op == '*':
            print("> "+str(f_n * s_n))
        elif op == '/':
            if f_n > s_n:
                print("> " + str(s_n / f_n))
            else:
                print("> " + str(f_n / s_n))
        elif op == '%':
            print("> "+str(f_n % s_n))
        else:
            print("Invalid Operation.")
            sys.exit()
    except ValueError:
        print("It's Invalid.")
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting Program.")
        sys.exit()
