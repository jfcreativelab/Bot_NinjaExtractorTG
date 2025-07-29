import asyncio
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest
from telethon.tl.types import ChannelParticipantsSearch, ChannelParticipantsAdmins
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
import os
import socket
import datetime

# ===== CONFIGS DO AUTOR ===== #
USUARIO_AUTORIZADO = "admin"
SENHA_AUTORIZADA = "jfcreativelab123"
LINK_VENDA = "https://pay.cakto.com.br/376xfep_501899"
NOME_AUTOR = "JFCREATIVELAB"

# ===== ARTE ASCII ===== #
ASCII_ART = """
                      .....                                                                           
                 :-++++++++++=:                                                                       
              .=**=:.  ..  .:=**=.      .----.                 --  :- -:       -:                     
             -#+.   -+##=:.    .+#=     :@*-*%: .::  .#-.     .%@= *# =- ..:. .+: .::.                
            +#:   :#@@%=.        .**    :@+.+%.-%+*#.+@*=     .%#%.*#.#+:%*+%+.%=.#++%:               
           +#.   .#%%@*-:          **   :@#+#*.*% :@-.@-      .%=***#.%+:@- #*.%= --=@-               
          :%.    +###*=-:      .::  %=  :@= :@= :@-.@-      .%=.%%#.%+:@- #*.%=-%--@-               
          **     +++++=---==-.  -*#:=#  :%*+#*.:#+**..*#=.::::.#= -%*.#=.%- **.%=-%++%-               
          #+     *+.-+#@@*+:.   .:: -%.   ...    ..    .. :--: .   .. .  .   .=@=  .                  
          **     .*+==+*+==-:  :-   =#  .+++=       .                .       .-:.++++= =++-           
          -%.   .:=#####.       *=. #+  :@=:..-..-.=%-.-:-.-=-  -=-.:%+: -=- .::::+@-.+%::%-          
           **  :.*=*%#-:    .:   . =#.  :@+=- ****.*%-:@*:=*-%-=%-*=-@+.*#-%+-@+: =%. *# ::.          
           .**:#+.=*%@*:   :-.    +#.   :@=:: .%@. =% .%: -+=%=*#   .%: %= **-%.  =%. *# =%=          
             +#+##:.=*+: .::    -**.    :@+--.***# -%-:@: ##-%==%-*=.%+.*#:%+-%.  =@. =%--@=          
              :+*%@*: .      :=**:      .--=-.-..-. --.-. :=--: -=-. :=: -=- .-   .-.  -=--.          
                .-+#%#====++*+=.                                                                      
                    .::--::.                                                                          
"""

# ===== BOAS-VINDAS ===== #
def boas_vindas():
    print(ASCII_ART)
    print("===============================================")
    print(f"🚀 Bem-vindo ao Bot_NinjaExtractorTG")
    print(f"🔐 Criado por: {NOME_AUTOR}")
    print(f"🛒 Adquira com acesso completo em: {LINK_VENDA}")
    print("===============================================\n")

# ===== LOGIN MANUAL ===== #
def autenticar():
    print("🔐 Acesso Restrito - Faça o Login para Usar o Script\n")
    for tentativa in range(3):
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == USUARIO_AUTORIZADO and senha == SENHA_AUTORIZADA:
            print("✅ Acesso autorizado! Bem-vindo!\n")
            gerar_log_acesso(usuario)
            return
        else:
            print("❌ Usuário ou senha incorretos.\n")

    print("🚫 Número máximo de tentativas. Encerrando script.")
    exit()

# ===== GERADOR DE LOGS ===== #
def gerar_log_acesso(usuario):
    try:
        ip_local = socket.gethostbyname(socket.gethostname())
    except:
        ip_local = "IP Não identificado"

    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{agora}] Usuário: {usuario} | IP: {ip_local}\n"

    with open("logs_acesso.txt", "a") as f:
        f.write(log_entry)

# ===== EXECUÇÃO INICIAL ===== #
boas_vindas()
autenticar()

# ======= CONFIGURAÇÕES =======
api_id = SUA API_ID  # <<< coloque sua api_id -> https://my.telegram.org/auth
api_hash = 'SUA API HASH'  # <<< coloque seu api_hash -> https://my.telegram.org/auth
session_name = 'mysession'

# Caminho para arquivos .txt
ADDED_USERS_FILE = 'usuarios_adicionados.txt'

# =============================

async def salvar_usuario_adicionado(username):
    with open(ADDED_USERS_FILE, 'a', encoding='utf-8') as f:
        f.write(username + '\n')

def carregar_usuarios_adicionados():
    if not os.path.exists(ADDED_USERS_FILE):
        return set()
    with open(ADDED_USERS_FILE, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f.readlines())

async def escolher_grupo(client, prompt):
    dialogs = await client.get_dialogs()
    grupos = [d for d in dialogs if getattr(d.entity, 'megagroup', False)]

    print(f'\n--- {prompt} ---')
    for i, g in enumerate(grupos):
        print(f'{i+1} - {g.name}')
    
    escolha = int(input(f'Selecione o número do grupo ({prompt}): ')) - 1
    return grupos[escolha]

async def obter_membros_normais(client, grupo):
    print(f'\n[+] Coletando membros do grupo: {grupo.name}')
    participantes = await client(GetParticipantsRequest(
        channel=grupo,
        filter=ChannelParticipantsSearch(''),
        offset=0,
        limit=10000,
        hash=0
    ))

    admins = await client(GetParticipantsRequest(
        channel=grupo,
        filter=ChannelParticipantsAdmins(),
        offset=0,
        limit=10000,
        hash=0
    ))
    ids_admins = {a.id for a in admins.users}

    membros = []
    for p in participantes.users:
        if not p.bot and p.username and p.id not in ids_admins:
            membros.append(p)
    
    print(f'[+] {len(membros)} membros normais encontrados.')
    return membros

async def adicionar_membros(client, membros, grupo_destino):
    adicionados = carregar_usuarios_adicionados()

    for usuario in membros:
        username = usuario.username.lower()
        if username in adicionados:
            print(f'[-] @{username} já adicionado anteriormente. Pulando...')
            continue

        try:
            print(f'[+] Adicionando @{username}...')
            await client(InviteToChannelRequest(
                channel=grupo_destino,
                users=[InputPeerUser(usuario.id, usuario.access_hash)]
            ))
            await salvar_usuario_adicionado(username)
            print(f'[✓] @{username} adicionado com sucesso.\n')
            await asyncio.sleep(5)  # Delay para evitar flood
        except PeerFloodError:
            print('[X] Erro: Flood detectado. Aguarde antes de tentar novamente.')
            break
        except UserPrivacyRestrictedError:
            print(f'[!] @{username} possui restrição de privacidade. Pulando...')
            continue
        except Exception as e:
            print(f'[!] Erro ao adicionar @{username}: {e}')
            continue

async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.connect()

        # Escolher grupo de origem
        grupo_origem = await escolher_grupo(client, 'Escolha o grupo de ORIGEM (de onde copiar membros)')
        membros = await obter_membros_normais(client, grupo_origem)

        # Escolher grupo de destino
        grupo_destino = await escolher_grupo(client, 'Escolha o grupo de DESTINO (para onde adicionar)')
        await adicionar_membros(client, membros, grupo_destino)

        print('\n✅ Fim do processo.')

if __name__ == '__main__':
    asyncio.run(main())