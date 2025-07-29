![Bot Status](https://img.shields.io/badge/NinjaExtractorTG-Online-success)
![Telegram API](https://img.shields.io/badge/Telegram-API-blueviolet)
![Project Type](https://img.shields.io/badge/Type-Automation-informational)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-Personal-lightgrey)
![Build](https://img.shields.io/badge/Build-Stable-brightgreen)

# 🥷 Bot_NinjaExtractorTG

Sistema Premium de **raspagem e adição de membros reais** entre grupos do Telegram com controle, segurança e comportamento humanizado.

---

## 📋 Sobre o Projeto

O **Bot_NinjaExtractorTG** conecta sua conta do Telegram via API, lista todos os grupos que você participa e permite:

- Extrair membros de um grupo de origem (com filtro pra evitar admins/donos)
- Adicionar membros de forma automatizada, com limite diário (49/dia)
- Logar tudo: quem foi adicionado, quando, e se já foi adicionado antes

⚠️ Todos os passos simulam o comportamento humano para evitar limites e punições.

---

## 🚀 Funcionalidades

- 📌 **Lista seus grupos automaticamente**
- 🔍 **Escolha o grupo de origem e destino**
- 🧼 **Ignora automaticamente admins e donos**
- 🧠 **Adiciona com delays e limites para simular humanos**
- ⏳ **Limite diário de 49 membros**
- ✅ **Evita membros repetidos com verificação automática**
- 🗂️ **Cria logs dos membros adicionados**
- 🔐 **Proteção via login e senha do criador**
- 🖥️ **Tela de boas-vindas estilizada com logo em ASCII**
- 📡 **Registro de IP/data/hora de cada acesso**

---

## 📂 Estrutura de Arquivos

```plaintext
raspador_telegram.py       # Script principal
adicionados.txt            # Usuários que já foram adicionados
adicionados_log.txt        # Registro com data/hora de quem foi adicionado
logs_acesso.txt            # Log de acessos ao sistema (IP/data)
