#ler a largura e aultura de uma parede e mostrar a área e a quantidade de tinta pra pintá-la sabendo que cada litro de tinta pinta 2 metros quadrados
lar = float(input("Qual é a largura da parede em metros? "))
alt = float(input("Qual é a altura da parede em metros? "))
area = lar*alt
print(f"A área da parede equivale a {area} metros quadrados")
print(f"Serão necessários {area/2} litros de tinta")