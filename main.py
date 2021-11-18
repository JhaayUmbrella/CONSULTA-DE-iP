import urllib.request, json
print('''\033[31m=============================
=JHAAY THE UMBRELLANO KID=
=============================\033[0;0m''')
ip = input("Root@Jhaay: ")

with urllib.request.urlopen(f"https://ipinfo.io/{ip}/json") as url:
    dados = json.loads(url.read().decode())
print("================================")
print('IP: ' + dados['ip'])
print('Nome da Host: ' + dados['hostname'])
print('Cidade: ' + dados['city'] + ' | Região: ' +dados['region'] + ' | País: ' + dados['country'])
print('Empresa Responsável: ' + dados['org'])
print('Endereço Postal: ' + dados['postal'])
print('TimeZone: ' + dados['timezone'])
print("=================================")
print('''\033[32mContato do Jhaay: 6791299030 Obrigado por usar volte sempre!!\033[1;92m''')
print("=================================")
print('''\033[36mNao me responsabilizo por atos de terceiros ao uso do programa!!\033[1;60m''')