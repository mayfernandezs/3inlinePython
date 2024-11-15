# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
def display_board(board):
  for i in range(len(board)):
    print("+-------+-------+-------+",end="\n")
    print("|       |       |       |",end="\n")
    for j in range(len(board[0])):
      print("|  ",board[i][j],"  ",end="")
    print("|",end="\n")
    print("|       |       |       |",end="\n")
  print("+-------+-------+-------+",end="\n")

# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
def enter_move(board):
  ocupado = True
  while ocupado:
    key_move = input("Elige una casilla libre: ")
    if not (key_move >="1" and key_move <="9") or len(key_move) > 1:
      print("\nLAS CASILLAS VAN DEL NÚMERO 1 AL 9\n")
      continue
    int_key_move = int(key_move)
    cell_move = board_positions[int_key_move]
    if cell_move in make_list_of_free_fields(board):
      ocupado = False
    else: 
      print("\n¡¡¡ESA CASILLA NO ESTÁ LIBRE!!!\n")
      ocupado = True
  x, y = cell_move
  board[x][y] = "O"
  display_board(board)
  victory_for(board,"O")
    
# La función examina el tablero y construye una lista de todos los cuadros vacíos. 
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
def make_list_of_free_fields(board):
    free_cells = []
    position = ()
    for i in range(len(board)):
      for j in range(len(board[0])):
        if (board[i][j] != "X" and board[i][j] != "O"):
          position = i,j,
          free_cells.append(position)
    return free_cells

# La función analiza el estatus del tablero para verificar si 
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
def victory_for(board, sign):
  win = False
  if board[0][0] == board[0][1] and board[0][0] == board[0][2] \
    or board[1][0] == board[1][1] and board[1][0] == board[1][2] \
    or board[2][0] == board[2][1] and board[2][0] == board[2][2] \
    or board[0][0] == board[1][0] and board[0][0] == board[2][0] \
    or board[0][1] == board[1][1] and board[0][1] == board[2][1] \
    or board[0][2] == board[1][2] and board[0][2] == board[2][2] \
    or board[0][0] == board[1][1] and board[0][0] == board[2][2] \
    or board[2][0] == board[1][1] and board[2][0] == board[0][2]:
    win = True      
  if win:
    if sign == "O":
        print("\n¡¡¡GANASTE!!!\n")
    else:
        print("\n¡¡¡PERDISTE!!!\n")
  else:
    if not len(make_list_of_free_fields(board)):
      print("\n¡¡¡EMPATE!!!\n")
    else:  
      if sign == "O":
        draw_move(board)
      else:
        enter_move(board)

# La función dibuja el movimiento de la máquina y actualiza el tablero.
def draw_move(board):
  from random import randrange
  input("Pulsa una tecla para el turno de la máquina")
  ocupado = True
  while ocupado:
    mach_move = randrange(1,10)
    mach_cell_move = board_positions[mach_move]
    if mach_cell_move in make_list_of_free_fields(board):
      ocupado = False
    else: 
      ocupado = True
  x, y = mach_cell_move
  board[x][y] = "X"
  display_board(board)
  victory_for(board,"X")

board = [[1,2,3],[4,"X",6],[7,8,9]]
board_positions = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
display_board(board)
enter_move(board)