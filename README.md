# Gemini-API-Alura
Curso Imersão IA Google Gemini

## Explicação do Código do Chatbot Gemini 🤖

O script cria um chatbot que usa a API Gemini do Google para responder perguntas do usuário.

Primeiro, ele carrega variáveis de ambiente do arquivo .env, buscando a chave da API (GEMINI_API_KEY). Se a chave não estiver configurada, o programa avisa e encerra para evitar erros.

Em seguida, configura o cliente da API Gemini com essa chave e inicializa o modelo generativo que vai criar as respostas.

Durante a execução, o chatbot entra em um loop que recebe perguntas do usuário via terminal. Se o usuário digitar "sair", o programa finaliza, salvando o histórico da sessão atual num arquivo de log com data e hora.

Para cada pergunta, o chatbot chama o modelo Gemini para gerar uma resposta. Essa resposta é exibida ao usuário e armazenada junto com a pergunta na lista de histórico da sessão.

Ao salvar o log, o programa escreve todas as interações da sessão no arquivo texto, facilitando acompanhar ou analisar depois as conversas.

O código ainda trata exceções, como erros na configuração da API ou na chamada para gerar respostas, garantindo que o programa não quebre e informe o problema ao usuário.

Em resumo, o código integra a API Gemini para criar um chatbot simples e funcional que mantém um histórico local das conversas para futuras consultas.
