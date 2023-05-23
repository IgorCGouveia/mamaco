#faça um programa que sorteie a ordem de aprsentação de trabalho de quatro alunos
import random
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)
print(f"A ordem de apresentação de trabalho vai ser {ordem}")