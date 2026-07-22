nome = "Anderson"
idade = 38
altura = 1.83
qa = True


print(nome)
print(idade)
print(altura)
print(qa)


linguagens = [
    "Python",
    "Javascript",
    "C#",
    "Java"
]

print(linguagens)
print(linguagens[0])
print(linguagens[1])

linguagens.append("Playwright")

print(linguagens)

usuario = {
    "nome": "Anderson",
    "idade": 37,
    "cargo": "QA"
}

print(usuario)

print(usuario["nome"])

usuario["empresa"] = "Aureka"
print(usuario)

idade = 15

if idade >= 18:
    print("Maior de Idade")
else:
    print("Menor de Idade")


for numero in range(5):
    print(numero)

for linguagens in linguagens:
    print(linguagens)

def somar(a , b):
    return a + b

resultado = somar(10,20)
print(resultado)

def boas_vindas(nome):
    print(f"Olá {nome}, seja bem vindo ao Bootcamp QA")

boas_vindas("Anderson")