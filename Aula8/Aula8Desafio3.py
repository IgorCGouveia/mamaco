#faça um programa que leia um angulo qualquer e mostre seu seno, cosseno e tangente
import math
ang = int(input("Digite o valor do ângulo: "))
s = math.sin(ang)
c = math.cos(ang)
t = math.tan(ang)
print("O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}".format(ang, s, c, t))
print(f"O ângulo de {ang} tem o seno de {s:.2f}, o cosseno de {c:.2f} e a tangente de {t:.2f}")