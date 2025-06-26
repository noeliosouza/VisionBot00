import json
from cryptography.fernet import Fernet

chave = Fernet.generate_key()
with open("chave.key", "wb") as chave_file:
    chave_file.write(chave)

fernet = Fernet(chave)

with open("config.json", "rb") as file:
    conteudo = file.read()

conteudo_cripto = fernet.encrypt(conteudo)
with open("config.enc", "wb") as file:
    file.write(conteudo_cripto)

print("✅ Configuração criptografada com sucesso!")
