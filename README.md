# 🤖 Vision Bot 00

Bot de automação para leitura de tela e apostas com estratégia baseada em cores. Inclui proteção por senha, criptografia de configuração e instalador opcional.

## ✅ Recursos
- Reconhecimento de cores azul/vermelho
- Estratégia fixa de sequência
- Meta de lucro automática
- Envio de alertas por Telegram
- Proteção por senha ao iniciar
- Configuração criptografada (`config.enc`)
- Histórico salvo e atualizado

## 🔒 Senha padrão
`noelio123`

## 🧪 Requisitos
- Python 3.10+
- Módulos:
  - `cryptography`
  - `pyinstaller` (se quiser compilar)

## 🚀 Compilando para EXE
```bash
pyinstaller --onefile --noconsole --icon=icon.ico --name="VisionBot00" visionbot.py
