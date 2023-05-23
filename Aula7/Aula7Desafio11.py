#Quantidade de KM percorridos pelo carro e quantos dias ele foi alugado, sabendo que cada dia custa 60 reais e cada KM custa 0,15
km = float(input("Quantos Km o carro percorreu? "))
d = int(input("Por quantos dias o carro foi alugado? "))
print(f"O valor total do alugel do carro foi de {(km*0.15) + (d*60)} reais")