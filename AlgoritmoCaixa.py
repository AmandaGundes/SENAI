#### Algoritmo Caixa D'água ####

quantidade = [] #controle da qntd de água em cada período
hora = 0 #contador de tempo
volume = 0 #caixa d'água vazia

import random
def vol(A, B):
  A = random.randint(1000,4000)
  B = random.randint(1000,3000)
  print(f'A quantidade da água que entrou é: {A} litros.')
  print(f'A quantidade da água que saiu é: {B} litros.')
  vol = A - B
  return vol

volume = 5000
quantidade.append(volume)

while volume < 100000:
  print(f'A quantidade inicial de água é: {volume} litros.')
  volume += vol(0, 0)
  quantidade.append(volume)
  hora +=1
  if volume > 100000:
    print('O volume neste momento é: 100000 litros.', '\n\n')
  elif volume < 0:
    print('O volume neste momento é: 0 litros.', '\n\n')
  else:
    print(f'O volume neste momento é: {volume} litros.', '\n\n')
  if volume <= 0:
    print(f'A caixa dágua está vazia. Levou {hora} horas para esvaziar por completo. O processo irá recomeçar.')
    volume = 0
    hora = 0
    quantidade.clear()
    quantidade.append(volume)

print(f'A caixa dágua está cheia. Levou {hora} horas para encher por completo. O volume de água que excedeu a capacidade total foi: {volume-100000} litros.', '\n\n')

#### FIM ####