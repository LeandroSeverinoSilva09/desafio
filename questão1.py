#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
#escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
#pertence ou não a sequência.

num = input("Digite um número:")

lista_fibonacci = [0, 1, 1, 2, 3]

def proximo_num():
    soma = lista_fibonacci[-1] + lista_fibonacci[-2]
    lista_fibonacci.append(soma)

while 1:
    if int(num) in lista_fibonacci:
        print (f"O número {num} pertence a sequência de Fibonacci")
        break
    proximo_num()
    if int(num) < lista_fibonacci[-1]:
        print (f"O número {num} não pertence a sequência de Fibonacci")
        break
    
    
    
    
