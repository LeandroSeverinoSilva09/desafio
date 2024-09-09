#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

palavra = input("Digite uma string: ")
qtd = 0
for i in palavra.lower():
    if i == 'a':
        qtd += 1
print(f"A quantidade de aparições de 'a' na palavra foi de {qtd} vezes")