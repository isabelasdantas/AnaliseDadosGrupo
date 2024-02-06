pessoas = homens = mulheres = 0
while True:
    idade = int(input('Qual é a idade: '))
    sexo = ' '
    while sexo not in "FM":
        sexo = str(input('Qual é o sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if idade <= 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'No grupo têm {pessoas} pessoa(as) maiores de 18 anos.')
print(f'Foram cadastrados {homens} homens no grupo.')
print(f'Foram cadastradas {mulheres} menos de 20 anos no grupo.')
