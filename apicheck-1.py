from requests import get
import os

#Slimakoi meu amado
#Lesanitu minha esposa
#SempreLEGIT melhor programador py
#Luffy Programmer todo os direitos reservados. ™

headers = {'NDCDEVICEID': 'null', 
    'NDCAUTH':'null'}
print(f'\033[95m┏━━━┓┏━━━┓┏━━┓')
print(f'\033[95m┃┏━┓┃┃┏━┓┃┗┫┣┛')
print(f'\033[95m┃┃╋┃┃┃┗━┛┃╋┃┃')
print(f'\033[95m┃┗━┛┃┃┏━━┛╋┃┃')
print(f'\033[95m┃┏━┓┃┃┃╋╋╋┏┫┣┓')
print(f'\033[95m┗┛╋┗┛┗┛╋╋╋┗━━┛')
print(f'\033[95m┏━━━┓┏┓╋┏┓┏━━━┓┏━━━┓┏┓┏━┓')
print(f'\033[95m┃┏━┓┃┃┃╋┃┃┃┏━━┛┃┏━┓┃┃┃┃┏┛')
print(f'\033[95m┃┃╋┗┛┃┗━┛┃┃┗━━┓┃┃╋┗┛┃┗┛┛')
print(f'\033[95m┃┃╋┏┓┃┏━┓┃┃┏━━┛┃┃╋┏┓┃┏┓┃')
print(f'\033[95m┃┗━┛┃┃┃╋┃┃┃┗━━┓┃┗━┛┃┃┃┃┗┓')
print(f'\033[95m┗━━━┛┗┛╋┗┛┗━━━┛┗━━━┛┗┛┗━┛')
print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
print(f"\033[96m                 \033[95mL U F F Y - P R O G R A M M E R          \033[96m       \033[1;00m")
print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
print(f"\033[96m        EXAMPLE:http://service.narvii.com/api/v1/x1/s/xxxxx")
print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
link = input('        API LINK: ')
def check_in(com_id):
    json = get(link, headers=headers).json()
    os.system('clear')
    print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
    print(f"\033[96m                 \033[95mL U F F Y - P R O G R A M M E R          \033[96m       \033[1;00m")
    print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
    print(f"\033[96m-> Duração da api:      {json['api:duration']}")
    print(f"\033[96m-> Retorno de mensagem: {json['api:message']}")
    print(f"\033[96m-> Time da Api:         {json['api:timestamp']}")
    print(f"\033[96m-> Código de status:    {json['api:statuscode']}")
    print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
    print(f"\033[96m      \033[95mM E - C O M E - L E S A N I T U - S E U - G O S T O S O          \033[96m       \033[1;00m")
    print(f"\033[96m                       \033[95mA P I - S T A T U S                \033[96m       \033[1;00m")
    print(f"\033[95m-----------------------------------------------------------------\033[1;00m")
check_in(1)