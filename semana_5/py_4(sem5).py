def divisores(num1):
    divisores = 0

    for i in range(1,num1 + 1):
        if num1 % i == 0:
            divisores += i

    return divisores
def main():
    num1 = 30

    print(divisores(num1))

main()