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