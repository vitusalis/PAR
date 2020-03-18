# PAR
# https://br.spoj.com/problems/PAR/
# Proposta de jogo com multiplas partidas de Par ou Impar

# O jogo possui validação de entrada dos dados assim como proposto e realiza múltiplas partidas
# em uma única simulação.

# O programa conta com três funções de: validação para nome do usuário, para os valores da jogada
# e separação das rodadas.

# Um problema encontrado foi a separação de valores através de mudança de linhas quando o texto é inserido pelo usuário,
# fazendo-se necessário a utilização de outro caracter para indicar
# a diferenciação dos dados, neste caso o hífen.

game = "3\nAlberto\nLucas\n2 5\n3 5\n1 1\n3\nCarlos\nMaria\n2 5\n3 5\n1 1\n4\nMarcos\nLeticia\n2 5\n3 5\n1 1\n2 4\n0".split("\n")
# game = input('Separe os dados com hifen (-)\nExemplo: 1-Joao-Maria-2 4-0\nEntre: ').split("-")


def validate_players(players):
  # Valida o nome dos jogadores de acordo com a regra: 'Um nome de jogador é uma cadeia de no mínimo um e no máximo dez letras (maiúsculas e minúsculas), sem espaços em branco'

  for player in (players):
    if (len(player)<1 or len(player)>10):
      return False

    for letter in player:
      if letter == ' ':
        return False
  return True

def validate_moves(move1, move2):
  # Valida o conjuto de jogadas de cada rodada de acordo com a regra: 
  # 0 <= A <= 5; 0 <= B <= 5
  for n in (move1, move2):
    if (n > 5 or n <= 0):
      return False
  return True


def separateRounds(game):
  # o fim da rodada atual é defida pelo início das jogadas feitas
  # (após o numero de rodadas e os nomes dos jogadores, consequentemente, *3*)
  # e pela quantidade de jogadas feitas, declarado no primeiro item do array *game[0]*

  game_ended = False
  game_rounds = []
  while (not game_ended):
    end = 3 + int(game[0]);
    g = game[0: end]

    # if last round
    if (g[-1] == '0'):
      game_ended = True
    else:
      game_rounds.append(g)
      game = game[end:]

  return game_rounds;


for game in separateRounds(game):
  rounds = game[0]
  player1= game[1]
  player2= game[2]
  moves  = game[3: ]

  # INPUT HANDLING 
  try:
    rounds = int(rounds);
    if (rounds <= 0 or rounds >= 1000):
      raise ValueError()

  except ValueError:
    print('Numero e jogadas inválido')
    raise
    
  if not validate_players([player1, player2]):
    raise Exception('Nome de jogador nao condiz com as regras')
    
  print()
  for item in moves:
    if (item) == '0':
      print("FIM")
    else:
      p1, p2 = item.split(' ')
      if not validate_moves(int(p1), int(p2)):
        raise Exception('Jogada inválida', item)
      winner = player1 if ((int(p1)+int(p2))%2) == 0 else player2
      print(winner)