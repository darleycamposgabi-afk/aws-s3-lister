import boto3

s3 = boto3.client('s3')


def listar_buckets():
    """Lista todos os buckets S3 da conta."""
    resposta = s3.list_buckets()
    buckets = resposta['Buckets']

    if not buckets:
        print("Nenhum bucket encontrado nessa conta.")
        return

    print(f"Você tem {len(buckets)} bucket(s):\n")
    for bucket in buckets:
        nome = bucket['Name']
        data_criacao = bucket['CreationDate']
        print(f"- {nome} (criado em {data_criacao})")


if __name__ == "__main__":
    listar_buckets()
    