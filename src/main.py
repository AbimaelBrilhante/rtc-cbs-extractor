import os
from dotenv import load_dotenv
from api_client import ReceitaFederalAPI

def main():
    # Carrega as variáveis do arquivo .env
    load_dotenv()
    
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    CNPJ_BASE = os.getenv("CNPJ_BASE")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")

    if not all([CLIENT_ID, CLIENT_SECRET, CNPJ_BASE, WEBHOOK_URL]):
        print("Erro: Verifique se todas as variáveis de ambiente estão configuradas no .env")
        return

    # Inicializa o cliente da API
    api = ReceitaFederalAPI(CLIENT_ID, CLIENT_SECRET, CNPJ_BASE, WEBHOOK_URL)

    try:
        # Passo 1: Obter Token
        token = api.obter_token()

        # Passo 2: Solicitar Apuração
        api.solicitar_apuracao(token)

        # Passo 3: Baixar Extrato (Descomente e insira o tíquete manual quando disponível)
        # tiquete_manual = "seu-tiquete-aqui"
        # api.baixar_extrato_json(token, tiquete_manual)

    except Exception as e:
        print(f"Erro no processo: {e}")

if __name__ == "__main__":
    main()
