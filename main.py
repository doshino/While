print ('\033[1m' + ' PROGRAMA - SEQUÊNCIA DE FIBONATTI' + '\033[0m')
print ("\n Na matemática, a sucessão de Fibonacci, é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. Ela se assemelha a proporção aurea que cria uma espiral infinita muito presente na natureza.")

print ("\n Legal né? Agora vamos testar, caso queira FINALIZAR O PROGRAMA DIGITE (0) abaixo ")

limite = int(input(" Digite o número de termos da sequência de Fibonacci que deseja calcular: "))


n1=0
n2=1
contador = 0
if limite==0:
    print('\033[1m' + '\n -- PROGRAMA FINALIZADO --' + '\033[0m')

while contador < limite:
    print(n1)  
    n1, n2 = n2, n1 + n2 
    contador += 1  