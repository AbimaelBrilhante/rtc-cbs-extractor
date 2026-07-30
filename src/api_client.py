import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ReceitaFederalAPI:
    def __init__(self, client_id, client_secret, cnpj_base, webhook_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.cnpj_base = cnpj_base
        self.webhook_url = webhook_url
        
        self.token_url = "https://api.receitafederal.gov.br/token"
        self.apuracao_url = f"https://api.receitafederal.gov.br/rtc/apuracao-cbs/v1/{self.cnpj_base}"
        self.download_base_url = "https://api.receitafederal.gov.br/rtc/download/v1/"
        
        self.headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json",
        }

    def obter_token(self):
        print("Solicitando Token...")
        response = requests.post(
            self.token_url,
            auth=(self.client_id, self.client_secret),
            data={"grant_type": "client_credentials"},
            headers=self.headers_base,
            verify=False,
            timeout=30,
        )
        if response.status_code == 200:
            print("Token obtido com sucesso.")
            return response.json().get("access_token")
        raise Exception(f"Erro no Token: {response.status_code} - {response.text}")

    def solicitar_apuracao(self, token):
        print(f"Solicitando arquivo para o CNPJ {self.cnpj_base}...")
        headers = {
            **self.headers_base,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        payload = {"urlRetorno": self.webhook_url}

        response = requests.post(
            self.apuracao_url, 
            headers=headers, 
            json=payload, 
            verify=False, 
            timeout=30
        )

        if response.status_code in [200, 201]:
            print(f"Solicitação aceita. Acompanhar retorno no Webhook: {self.webhook_url}")
        else:
            print(f"Erro na Apuração: {response.status_code} - {response.text}")

    def baixar_extrato_json(self, token, tiquete_download):
        print(f"Baixando JSON com o Tíquete: {tiquete_download}...")
        url_download = f"{self.download_base_url}{tiquete_download}"
        headers = {
            **self.headers_base,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        response = requests.get(url_download, headers=headers, verify=False, timeout=30)

        if response.status_code == 200:
            dados_json = response.json()
            nome_arquivo = f"apuracao_cbs_{self.cnpj_base}.json"
            
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                json.dump(dados_json, f, indent=2, ensure_ascii=False)
                
            print(f"SUCESSO! Arquivo salvo como '{nome_arquivo}'.")
            return dados_json
        else:
            print(f"Erro no Download: {response.status_code} - {response.text}")
