def eh_primo(num1):

    if num1 % 2 == 0:
        return False
    
    for i in range(3,num1):
        if num1 % i == 0:
            return False

    return True

def main():
    num1 = int(input('Digite um número:\n--> '))

    output = eh_primo(num1)
    print(output)

main()