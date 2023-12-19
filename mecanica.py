import random
from visual import *

VEICULO_ALTURA = 250



def alternar_faixa(carro_posicao, faixa):
  carro_posicao.center = (faixa, carro_posicao.center[1])

# Questão 5, item 1
def mover_adversario_aleatoriamente(carro_posicao, velocidade):
  carro_posicao[1] += velocidade
  global faixa
  
  
  # Questão 5, itens 3, 4 e 5
  if carro_posicao[1] > JANELA_ALTURA:
    carro_posicao[1] = -250
    
    
    faixa = random.randint(0, 1)
    if faixa == 0:
      alternar_faixa(carro_posicao, FAIXA_ESQUERDA)
    if faixa == 1:
      alternar_faixa(carro_posicao, FAIXA_DIREITA)
    

  return carro_posicao
   

# Questão 7, item 1
def houve_colisao(carro_posicao, carro2_posicao):
  if carro_posicao[0]==carro2_posicao[0] and carro2_posicao[1] + VEICULO_ALTURA >= carro_posicao[1]:
    return True   
  else:
    return False

     



# Questão 8, item 1
def subir_nivel(velocidade):
  velocidade = velocidade + 0.5 
  print (f"Subiu de nível - Velocidade{velocidade}")
  return velocidade