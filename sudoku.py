tabela = [
    [0,0,0,0,0,0,0,2,0],
    [6,0,0,0,0,7,0,0,0],
    [0,0,7,0,8,0,0,0,1],
    [0,8,0,0,0,0,2,0,0],
    [0,1,0,9,0,0,0,8,4],
    [0,0,0,0,1,0,3,0,9],
    [0,0,2,0,0,0,9,0,0],
    [0,0,8,7,0,3,6,0,0],
    [7,0,9,6,0,4,0,0,0]
]

def solucionador(tab):
		
	procure = procure_vazio(tab)

	if not procure:
		return True
	else:
		linha, coluna = procure

	for i in range(1,10):
		if valido(tab, i, (linha, coluna)):
			tab[linha][coluna] = i
			
			if solucionador(tab):
				return True

			tab[linha][coluna] = 0
	
	return False




def valido(tab, num, pos):
	
	# Checagem da linha
	for i in range(len(tab[0])):
		if tab[pos[0]][i] == num and pos[1] != i:
			return False

	# Checagem da coluna
	for i in range(len(tab)):
		if tab[i][pos[1]] == num and pos[0] != i:
			return False
		 
	# Checagem do bloco
	bloco_x = pos[1] // 3
	bloco_y = pos[0] // 3

	for i in range(bloco_y * 3, bloco_y * 3 + 3):
		for j in range(bloco_x * 3, bloco_x * 3 + 3):
			if tab[i][j] == num and (i,j) != pos:
				return False
	return True


def print_tabela(tab):
	
	for i in range(len(tab)):
		if i % 3 == 0 and i != 0:
			print("-----------------------")

		for j in range(len(tab[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end="")

			if j == 8:
				print(tab[i][j])
			else:
				print(str(tab[i][j]) + " ", end="")

def procure_vazio(tab):

	for i in range(len(tab)):
		for j in range(len(tab[0])):
			if tab[i][j] == 0:
 				return(i, j) #Linha e coluna 
	return None

print("\n_______________________")
print_tabela(tabela)
solucionador(tabela)
print("\n_______________________")
print_tabela(tabela)
