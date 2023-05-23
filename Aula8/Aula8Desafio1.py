#cria um programa que leia um numero real qualquer e mostre sua porção inteira
import math
num = float(input("Digite um número: "))
print(f"O número digitado foi {num} e sua porção inteira é {math.trunc(num)}")