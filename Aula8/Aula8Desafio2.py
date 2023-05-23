#faça um programa que leia o comprimento dos catetos, calcule e mostre a hipotenusa
import math
cateto1 = float(input('Digite o comprimento do cateto 1: '))
cateto2 = float(input("Digite o comprimento do cateto 2: "))
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
print(f"Em um triângulo retangulo no qual os catetos são {cateto1} e {cateto2} a hipotenusa é {hipotenusa}")