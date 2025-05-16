import google.generativeai as genai
import os
from datetime import datetime
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configurações ---
API_KEY = os.getenv("GEMINI_API_KEY")
NOME_ARQUIVO_LOG = "interacoes_chatbot.txt"

if not API_KEY:
    print("ERRO: Chave API da Gemini não encontrada.")
    print("Por favor, crie um arquivo .env com GEMINI_API_KEY='SUA_CHAVE_AQUI'")
    exit()

# Configura o cliente da API Gemini
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.0-pro-latest') # ou 'gemini-pro'
except Exception as e:
    print(f"Erro ao configurar ou inicializar o modelo Gemini: {e}")
    exit()

# Lista para guardar as interações da sessão atual
historico_sessao_atual = []

def salvar_log_interacoes(interacoes_para_salvar):
    """Salva as interações da sessão atual no arquivo de log."""
    try:
        with open(NOME_ARQUIVO_LOG, "a", encoding="utf-8") as arquivo_log:
            timestamp_sessao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivo_log.write(f"\n--- Nova Sessão Iniciada em: {timestamp_sessao} ---\n")
            for interacao in interacoes_para_salvar:
                arquivo_log.write(f"Usuário: {interacao['pergunta']}\n")
                arquivo_log.write(f"Chatbot: {interacao['resposta']}\n")
                arquivo_log.write("-" * 30 + "\n")
        print(f"Interações salvas em '{NOME_ARQUIVO_LOG}'.")
    except IOError as e:
        print(f"Erro ao salvar o log: {e}")

def iniciar_chat():
    """Função principal que executa o chatbot."""
    print("Olá! Sou seu chatbot Gemini. Faça uma pergunta ou digite 'sair' para terminar.")

    while True:
        pergunta_usuario = input("Você: ").strip()

        if pergunta_usuario.lower() == "sair":
            print("Chatbot: Até mais! Salvando nossa conversa...")
            if historico_sessao_atual: # Só salva se houver interações
                salvar_log_interacoes(historico_sessao_atual)
            else:
                print("Nenhuma interação nesta sessão para salvar.")
            break # Encerra o loop e o programa

        if not pergunta_usuario: # Se o usuário apenas pressionar Enter
            print("Chatbot: Por favor, digite algo.")
            continue

        try:
            # Gera a resposta usando a API Gemini
            resposta_modelo = model.generate_content(pergunta_usuario)
            resposta_chatbot = resposta_modelo.text
        except Exception as e:
            resposta_chatbot = f"Desculpe, ocorreu um erro ao tentar obter uma resposta: {e}"
            print(f"DEBUG: Erro da API: {e}") # Para depuração

        print(f"Chatbot: {resposta_chatbot}")

        # Registra a interação atual na lista da sessão
        historico_sessao_atual.append({
            "pergunta": pergunta_usuario,
            "resposta": resposta_chatbot
        })

if __name__ == "__main__":
    iniciar_chat()
