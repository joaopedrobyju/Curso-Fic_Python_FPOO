cidade_saida = input("A cidade de saída é: ")
cidade_destino = input("A cidade de destino é: ")
distância = input("A distância é de: ")
km_litro = input("O consumo é de: ")
combustivel_tipo = input("O tipo de combustível é:")
valor = input("o valor do combustivel é de: ")

media = (float(distância) / float(km_litro) * float(valor))

print("As informações são:\n")
print(cidade_saida)
print(cidade_destino)
print(distância)
print(km_litro)
print(combustivel_tipo)
print(valor)
print("A média é de", media)