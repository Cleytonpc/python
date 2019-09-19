def resultado (time1, time2):
    if rtime1 > rtime2:
        print ('Vencedor:', time1)
        return time1
    elif rtime2 > rtime1:
        print ('Vencedor:', time2)
        return time2
    else:
        print('Empate!')
        return 'empate'



times = {'athletico paranaense': 0, 'atletico mineiro': 0, 'avai': 0, 'bahia': 0, 'botafogo': 0, 'csa': 0, 'ceara': 0, 'chapecoense': 0, 'corinthians': 0, 'cruzeiro': 0, 'flamego': 0, 'fluminense': 0, 'fortaleza': 0, 'goias': 0, 'gremio': 0, 'internacional': 0, 'palmeiras': 0, 'santos': 0, 'sao paulo': 0, 'vasco': 0}

print ('Jogos brasileirão')
print ('Times na competição: athletico paranaense, atletico mineiro, avai, bahia, botafogo, csa, ceara, chapecoense, corinthians, cruzeiro, flamego, fluminense, fortaleza, goias, gremio, internacional, palmeiras, santos, sao paulo, vasco')



continuar = True

while continuar == True:
    val_gol = False
    val_time = False
    ##    validação se o time esta na lista
    while val_time == False:
        time1 = input('Informe o time mandante: ').lower()
        if time1 in times:
            val_time = True
            while val_gol == False:
                rtime1 = input ('Informe a quantidade de gols do mandante: ')
                try:
                    rtime1 = int(rtime1)
                    if rtime1 < 0:
                        print ("O numero de gols não pode ser menor que '0'.")
                    else:
                        val_gol = True
                except:
                    print('Informe um valor valido, ultisando apenas numeros inteiros.')
        else:
            print('Time não localizado,Infome um time presente no campeonato(informar sem assentos)')
    val_time = False
    val_gol = False
    while val_time == False:
        time2 = input('Informe o time visitante: ').lower()
        if time2 in times and time2 != time1:
            val_time = True
            while val_gol == False:
                rtime2 = input ('Informe a quantidade de gols do visitante: ')
                try:
                    rtime2 = int(rtime2)
                    if rtime2 < 0:
                        print ("O numero de gols não pode ser menor que '0'.")
                    else:
                        val_gol = True
                except:
                    print('Informe um valor valido, ultisando apenas numeros inteiros.')
        else:
            print('Time não localizado(informar sem assentos),Infome um time presente no campeonato. Não informar o mesmo time nos dois campos!')

    vencedor = resultado(time1, time2)

    if vencedor == 'empate':
        times[time1] = times[time1] + 1
    else:
        times[vencedor] = times[vencedor] + 3
    val = False
    while val == False:
        r = input ('Deseja Informar o resultado de mais algum jogo? (S/N)').lower()
        if r == 's' or r == 'n':
            val = True
        else:
            print (" use 'S' para sim e 'N' para não.")
            continue
    if r == 's':
        continue
    else:
        continuar = False
print ('\n')
for x in sorted ( times, key = times.get, reverse = 1):
    print (x, '-', times[x])
