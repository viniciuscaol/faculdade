nome = 'exemplo de string em python'
print(nome,type(nome))
print('valor da variavel nome = {}'.format(nome))
print(f'valor da variavel nome = {nome}')

# Atribuição Multipla
a, b = 1, 2
print ('Antes da troca')
print(f'O valor das variaveis: a={a}, b={b}')
# Primeira Troca
temp = a
a = b
b = temp
print('Primeira troca')
print(f'O valor das variaveis: a={a}, b={b}')
# Segunda Troca
a, b = b, a
print('Segunda troca')
print(f'O valor das variaveis: a={a}, b={b}')

# Operadores compostos

x=10
print(f'x={x}',type(x))
x+=2
print(f'x={x}')
x-=2
print(f'x={x}')
x*=2
print(f'x={x}')
x/=2
print(f'x={x}',type(x))
x%=2
print(f'x={x}')

def func():
    x = 1
    print(x)

func()
print(x)