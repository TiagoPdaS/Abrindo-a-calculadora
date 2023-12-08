import pyautogui as posicaoMouse
import pyautogui as tempoEspera 

print('Robô Inicializado...')

# clicando na pesquisa
tempoEspera.sleep(2)    

#clicando na pesquisa
posicaoMouse.click(619, 1047)

#escrevendo a pesquisa
tempoEspera.sleep(2)
posicaoMouse.typewrite('calculadora')
tempoEspera.sleep(1)

#clicando na opção
tempoEspera.sleep(1)
posicaoMouse.click(700, 271)

""" AQUI ESTA EM COMENTARIO A SOMA DOS VALORES, ENTAO 
SO VAI ABRIR A MINHA CALCULADORA

#clicando no primeiro valor
tempoEspera.sleep(2)
posicaoMouse.click(301, 571)

#escolhendo a função matematica
tempoEspera.sleep(1)
posicaoMouse.click(377, 553)

#escolhendo outro valor
tempoEspera.sleep(1)
posicaoMouse.click(227, 504)

#clicando no botão de resultado
tempoEspera.sleep(1)
posicaoMouse.click(387, 613)
#print(posicaoMouse.position())

"""

print('Robô Desligado...')