"""
UNIVERSIDADE FEDERAL FLUMINENSE
HIGH PRECISION AD/DA BOARD INTEGRATED ON RASPBERRY PI 4
RESEARCHER: WEBER GAIA
"""

import time
import ADS1256
import matplotlib.pyplot as plt
import numpy as np
#import RPi.GPIO as gpio

ADC = ADS1256.ADS1256()                                 # Criando objeto para inicializar o ADC
ADC.ADS1256_init()                                      # Chamada de função de inicialização
ADC.ADS1256_ConfigADC(0,0xF0)                           # Ganho e taxa de amostragem
        
for i in range(5,-1,-1):                                # Contagem regressiva para iniciar a coleta de dados
    print(f"Iniciando a coleta em {i}s...")
    time.sleep(1)

lista = [];                                             # Variável de armazenamento de valores
for i in range(0,500,1):                                # Loop para iniciar a coleta de dados
    canal = ADC.ADS1256_GetChannalValue(0)              # Configurando o canal AD0 para coletar
    conv = (canal*5.0/0x7fffff)                         # Conversão analógica-digital
    lista.append(conv)                                  # Armazenando valores na lista
    #print (f"{conv:.8f} V")

x = np.arange(0,len(lista))                             # Valores para o eixo X
plt.plot(x,lista)                                       # Plotagem gráfica da coleta de dados
plt.grid(True)                                          # Exibição de grades
plt.show()                                              # Plotar figura