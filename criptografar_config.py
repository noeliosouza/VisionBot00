import json
from cryptography.fernet import Fernet

# Gerar chave e salvar no arquivo chave.key
chave = Fernet.generate_key()
with open("chave.key", "wb") as chave_file:
    chave_file.write(chave)

fernet = Fernet(chave)

# Ler o arquivo config.json (configuração normal)
with open("config.json", "rb") as file:
    conteudo = file.read()

# Criptografar o conteúdo do config.json
conteudo_cripto = fernet.encrypt(conteudo)

# Salvar o conteúdo criptografado no arquivo config.enc
with open("config.enc", "wb") as file:
    file.write(conteudo_cripto)

print("✅ Arquivos chave.key e config.enc gerados com sucesso!")
