# loT-ThingSpeak-Python
Trabalho de Extensão sobre Aplicações de Cloud, IoT e Indústria 4.0 em Python

Este projeto aborda o uso do ThingSpeak em uma simulação de IoT. Vou guiá-lo através de um tutorial para simular dispositivos IoT e enviar dados de sensores para o ThingSpeak. Utilizaremos uma placa como o ESP8266 (ou simulação) e o Arduino IDE para escrever o código. Caso não tenha o hardware disponível, é possível simular a lógica do projeto.

## Etapas do Projeto

1. **Criação de uma Conta no ThingSpeak**
2. **Configuração de um Canal ThingSpeak**
3. **Escrever o Código para Enviar Dados**
4. **Visualizar Dados em Gráficos no ThingSpeak**

### 1. Criar uma Conta no ThingSpeak

- Vá para o [ThingSpeak](https://thingspeak.com) e crie uma conta gratuita.
- Após o registro, faça login e acesse o Painel de Controle.

### 2. Configuração de um Canal ThingSpeak

- No painel do ThingSpeak, clique em **Channels** (Canais) e depois em **New Channel** (Novo Canal).
- Preencha as informações do seu canal:
  - **Nome do Canal**: Dê um nome ao seu projeto.
  - **Campos**: Defina os campos para os dados que você vai enviar. Por exemplo, se estiver simulando um sensor de temperatura, insira "Temperatura" no campo Field 1.
- Clique em **Save Channel**.
- Após salvar o canal, você verá uma página com um gráfico que exibirá os dados. Anote a **Write API Key**, pois ela será usada para autenticar o envio de dados.

### 3. Escrever o Código para Enviar Dados

Agora, criaremos o código para enviar dados simulados para o ThingSpeak.

#### Exemplo de Código usando Arduino IDE e ESP8266 (ou simulação de envio de dados):

1. Abra o Arduino IDE.
2. Instale a biblioteca ThingSpeak e ESP8266 (caso use hardware).
   - Vá em **Sketch** > **Include Library** > **Manage Libraries** e procure por ThingSpeak. Depois, instale a biblioteca.
3. Use o código de [exemplo](https://github.com/GabrielArthur/loT-ThingSpeak-Python/blob/main/exemplo_enviar_dados.py) para enviar dados ao ThingSpeak.

### 4. Visualizar os Dados no ThingSpeak

Depois de usar o código de exemplo para enviar os dados para o ThingSpeak:

- Vá até seu canal no ThingSpeak.
- Os dados enviados serão exibidos como gráficos, conforme você os envia a partir do código.
- Você pode configurar widgets e gráficos adicionais para exibir os dados de formas diferentes.

### Conclusão

Utilizando o ThingSpeak, você pode facilmente simular um projeto IoT com hardware real ou apenas via simulação. ThingSpeak é uma ótima ferramenta para começar a visualizar dados de sensores na nuvem e oferece suporte a diversos tipos de dispositivos.
