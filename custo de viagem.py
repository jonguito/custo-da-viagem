viagem = float(input('Qual é a distância da sua viagem?:  '))
limite_200km = (viagem * 0.50  ) 
viagens_longas = (viagem * 0.45 ) 
if viagem <= 200:
    print(f'''Você está prestes a começar uma viagem de {viagem}km
e o preço da sua viagem será de R${limite_200km :.2f}''')
if viagem >200:
    print(f'''Você está prestes a começar uma viagem de {viagem}km
e o preço da sua viagem será de R${viagens_longas:.2f}''')
