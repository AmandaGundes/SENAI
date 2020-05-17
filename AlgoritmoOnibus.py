#### Algoritmo Ônibus ####

passageiros = [] #controle de passageiros no ônibus em cada momento
pessoas = 0 #pessoas dentro do ônibus
pessoasfora = 0 #pessoas que não conseguiram entrar no ônibus
ponto = list(range(2, 20)) #pontos de parada
embarque = 0 #qntd de pessoas que viajaram no ônibus


import random
def entradaonibus(A):
  A = random.randint(0,7)
  entradaonibus = A
  return entradaonibus
def saidaonibus(B):
  B = random.randint(0,5)
  saidaonibus = B
  return saidaonibus

pessoas = entradaonibus(0) #pessoas que subiram no primeiro ponto
print(f'A quantidade de pessoas que subiu no primeiro ponto é: {pessoas}', '\n\n')
passageiros.append(pessoas)
embarque = pessoas

for i in ponto:
  p1 = entradaonibus(0)
  p2 = saidaonibus(0)
  pessoas += p1-p2
  embarque += p1
  if pessoas < 44 and pessoas > 0:
    passageiros.append(pessoas)
    print(f'A quantidade de passageiros que subiu é: {p1}')
    print(f'A quantidade de passageiros que desceu é: {p2}')
    print(f'Existem {pessoas} pessoas dentro do ônibus.', '\n\n')
  elif pessoas >= 44:
    pessoasfora = pessoas-44
    p1 = pessoas-pessoasfora-p2
    passageiros.append(44)
    print(f'A quantidade de passageiros que subiu é: {p1}')
    print(f'A quantidade de passageiros que desceu é: {p2}')
    print(f'O ônibus está lotado com 44 pessoas. Deixaram de embarcar {pessoasfora} pessoas no ônibus.', '\n\n')
  else:
    while pessoas <= 0:
      print(f'A quantidade de passageiros que subiu é: {p1}')
      print(f'A quantidade de passageiros que desceu é: {p2}')
      print('O ônibus ficou vazio. Aguardar pessoas entrar.')
      pessoas = entradaonibus(0)
      p1 = pessoas
      passageiros.append(pessoas)
      print(f'A quantidade de pessoas que subiu é: {pessoas}', '\n\n')
  continue

print(f'A quantidade de pessoas que desceu no último ponto foi: {passageiros[-1]}', '\n')
print(f'O total de passageiros que viajou no ônibus foi: {embarque}')

#### FIM #####