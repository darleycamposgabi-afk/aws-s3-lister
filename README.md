# AWS S3 Bucket Lister

Script em Python que se conecta à AWS via boto3 e lista todos os buckets S3 disponíveis na conta, exibindo nome e data de criação de cada um.

## Tecnologias

- Python 3
- boto3 (AWS SDK for Python)
- AWS S3

## Como funciona

O script usa o cliente `boto3.client('s3')` para se autenticar com a AWS (usando as credenciais configuradas via `aws configure`) e chama o método `list_buckets()`, que retorna todos os buckets da conta.

## Pré-requisitos

- Conta AWS (free tier funciona)
- Python 3.8+
- AWS CLI instalado e configurado (`aws configure`)

## Como rodar

```bash
# Clone o repositório
git clone https://github.com/SEU-USUARIO/aws-s3-lister.git
cd aws-s3-lister

# Crie e ative um ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
source venv/bin/activate      # Mac/Linux

# Instale as dependências
pip install boto3

# Configure suas credenciais AWS (se ainda não fez)
aws configure

# Execute
python s3_lister.py
```

## Próximos passos

- Adicionar tratamento de erros (credenciais inválidas, sem permissão, etc.)
- Permitir criar e deletar buckets via script
- Adicionar testes automatizados

## Autora

Darley Campos