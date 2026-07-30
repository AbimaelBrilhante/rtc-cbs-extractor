# Brazilian Tax Reform (RTC) - CBS Data Extractor

This project automates the extraction of tax data related to the Contribuição sobre Bens e Serviços (CBS) using the Receita Federal (Brazilian IRS) API

## 📌 Business Context
With the recent Tax Reform on Consumption (RTC), Brazil created two new taxes, including the CBS which is under federal responsibility This new model replaces traditional manual tax declarations with automated data extraction directly from electronic invoices (Documentos Fiscais Eletrônicos)

This script specifically interacts with the **Apuração Assistida** system The Apuração Assistida is a system developed by the tax authority to verify and calculate a taxpayer's operations in an automated and transparent way

*Note: The platform is currently operating in a Beta Environment for the year 2026, allowing companies to simulate integrations without generating real tax liabilities

## 🚀 Technical Architecture
The pipeline is designed to authenticate, request, and download tax data in a machine-readable JSON format The data flow follows these steps:

1. **Authentication:** Generates an access token using OAuth2 client credentials via the `/token` endpoint
2. **Data Request:** Submits an asynchronous request to the CBS calculation endpoint. The API requires a webhook URL to send the processing status back to our system
3. **Download:** Once the ticket is received via the webhook, the script hits the download endpoint to retrieve the JSON file containing the CBS debit records

## 🛠️ Technologies & Skills Demonstrated
* **Python 3:** Core language for the API integration.
* **REST API:** Handling `GET` and `POST` requests, authentication headers, and JSON payloads.
* **Security:** Use of `.env` files to hide sensitive information (Client ID, Client Secret, CNPJ).
* **Domain Knowledge:** Deep understanding of the Brazilian tax system, SAP integrations, and financial compliance.

## ⚙️ How to Run
1. Clone this repository.
2. Install the required libraries: `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example` and add your secure credentials.
4. Run the main script: `python src/main.py`
