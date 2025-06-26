import json, getpass
from cryptography.fernet import Fernet

senha_correta = "noelio123"
senha = getpass.getpass("🔐 Digite a senha para iniciar o Vision Bot: ")
if senha != senha_correta:
    print("❌ Senha incorreta. Encerrando...")
    exit()

with open("chave.key", "rb") as chave_file:
    chave = chave_file.read()
fernet = Fernet(chave)

with open("config.enc", "rb") as file:
    config_decifrado = fernet.decrypt(file.read()).decode()

config = json.loads(config_decifrado)

print("✅ Vision Bot 00 iniciado com sucesso!")
print("⚙️ Config carregada:", config)

# aqui entra seu código de apostas...
