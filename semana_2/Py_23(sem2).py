num1 = int(input("\nDigite um número: "))

print(f"O número {num1} é {'par.' if (num1 % 2 == 0) else 'ímpar.'}")

nota = int(input("\nDigite a nota: "))

print(f'{"Nota inválida" if nota > 10 or nota < 0 else "APROVADO." if nota >= 6 else "REPROVADO." if nota < 6 else ''}')

nota2 = int(input("\nDigite a nota 2: "))

print(f'{"Nota inválida." if nota2 > 10 or nota2 < 0 else "APROVADO." if nota2 >= 7 else "RECUPERAÇÃO." if nota >= 5 else "REPROVADO." }')

num2 = int(input("\nDigite um número: "))

print(f"O número {num2} é {'positivo.' if num2 > 0 else 'negativo.' if num2 < 0 else 'zero.'}")