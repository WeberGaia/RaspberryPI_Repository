## Repositório dedicado à utilização do Raspberry Pi 4 com o conversor analógico-digital "High precision AD/DA board"

Abaixo, seguem as informações para o funcionamento do conversor ADS1256 e o Raspberry PI 4:<br>

1- Instalar a imagem do Raspberry Pi e realizar as configurações necessárias.<br>

2- Instalar a interface para a linguagem que melhor o leitor se adaptar. Neste caso, podendo utilizar Python e linguagem C.<br>

3- Acessar o site [Waveshare](https://www.waveshare.com/wiki/High-Precision_AD/DA_Board?spm=a2g0o.detail.1000023.5.7b9429ccfk2OOy) para verificar todas as configurações necessárias de conexão do conversor.<br>

4- Instalar as [bibliotecas das linguagens](https://www.waveshare.com/wiki/Libraries_Installation_for_RPi) para o melhor funcionamento do código.<br>

5- Após ler atentamente as configurações necessárias do passo 3, acessar o [Github]( https://github.com/waveshare/High-Precision-AD-DA-Board) recomendado pela fabricante e estudar com detalhes os códigos da linguagem que achar melhor.<br>
<strong>OBS: Se você possuir o Raspberry PI, acesse somente a pasta direcionada a ele. Jetson nano é um dispositivo equivalente ao RPi e não uma biblioteca.</strong><br>

6- Ao acessar as pastas, verificar os arquivo ADS1256.py, main.py e config.py.<br>

7- Manter estes três arquivos juntos em um mesmo diretório, senão o arquivo padrão não será debbugado.<br>

8- O código, no repositório acima, é direcionado para leitura analógica de um potenciometro externo ao do conversor ADS1256.
<br>



## Repository dedicated to using the Raspberry Pi 4 with the "High precision AD/DA board" analog-digital converter

Below, follow the information for the operation of the ADS1256 converter and the Raspberry PI 4:<br>

1- Install the Raspberry Pi image and perform the necessary settings.<br>

2- Install the interface for the language that the reader adapts best. In this case, you can use Python and C language.<br>

3- Access the website [Waveshare](https://www.waveshare.com/wiki/High-Precision_AD/DA_Board?spm=a2g0o.detail.1000023.5.7b9429ccfk2OOy) to check all necessary converter connection settings.<br >

4- Install the [Language Libraries](https://www.waveshare.com/wiki/Libraries_Installation_for_RPi) for the best functioning of the code.<br>

5- After carefully reading the necessary settings in step 3, access the [Github](https://github.com/waveshare/High-Precision-AD-DA-Board) recommended by the manufacturer and study in detail the language codes that find better.<br>
<strong>NOTE: If you have the Raspberry PI, access only the folder directed to it. Jetson nano is an RPi equivalent device and not a library.</strong><br>

6- When accessing the folders, check the ADS1256.py, main.py and config.py files.<br>

7- Keep these three files together in the same directory, otherwise the default file will not be debugged.<br>

8- The code, in the repository above, is directed to the analog reading of a potentiometer external to the ADS1256 converter.
