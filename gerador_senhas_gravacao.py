"""
Escreva um programa que gere uma senha aleatória com um determinado comprimento. A senha deve conter uma mistura de letras, números e caracteres especiais. O comprimento da senha deve ser fornecido pelo usuário. Se o comprimento for menor que 4, imprima uma mensagem de erro e peça ao usuário para fornecer um novo comprimento.

A senha deve ser aleatória, então cada vez que o usuário executar o programa, uma nova senha deve ser gerada. Obrigatoriamente, a senha deve conter pelo menos uma letra, um número e um caractere especial. A senha não pode conter espaços em branco.

O programa deve conter uma função chamada `gerar_senha` que recebe o comprimento da senha como parâmetro e retorna a senha gerada. Se o comprimento for inválido, a função deve retornar None.

Exemplo de saída:

```
Digite o comprimento da senha: 10
8Zn$*2q9X
```

- Dica: use a biblioteca random e a função shuffle para embaralhar os caracteres da senha.
- Dica: use a função choice, dessa mesma biblioteca, para escolher um caractere aleatório de uma string.
- Dica: use a biblioteca string para obter uma lista de caracteres válidos para a senha.
"""

# importando bibliotecas
import string, random

# Montando uma string contendo letras números e caracteres especiais
lista_de_strings = [string.ascii_letters, string.digits, string.punctuation]

# "Randomizando" a lista para evitar que a senha comece sempre com letras, ou números, ou caracteres especiais através random.shuffle()

def gerar_senha(num_caracteres):
    if num_caracteres < 4:
        print("A senha deve ter pelo menos 4 caracteres.")
    else:
        # De forma aleatória serão escolhidas: letra, numero e caracter especial 
        letra = random.choice(string.ascii_letters)
        numero = random.choice(string.digits)
        caracter_especial = random.choice(string.punctuation)
        
        # Cria-se uma lista com uma letra, um numero e um caracter especial.
        lista_de_caracteres = [letra, numero, caracter_especial]
        
        # Cria-se, de forma concatenada uma string contendo todos o números, letras e caractere especiais
        string_de_caracteres = "".join(lista_de_strings)
        
        # Através do random.choices serão escolhidos os caracteres restantes da diferença entre k = num_caracteres - 3
        # O método extend da lista irá adicioná-los à lista_caracteres 
        lista_de_caracteres.extend(random.choices(string_de_caracteres, k = num_caracteres - 3))
        
        # Shuffle irá embaralhar a lista_de_senhas
        random.shuffle(lista_de_caracteres)
        
        # Será retornada uma string da lista_de_caracteres através do "".join() 
        return "".join(lista_de_caracteres)
        
tamanho_da_senha = int(input("Escolha a quantidade de caracteres para gerar a senha: "))
print(gerar_senha(tamanho_da_senha))

