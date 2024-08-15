import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, o jogo "The Last of Us Part II" foi lançado em 2020.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, "Ghost of Tsushima" foi lançado em 2020.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, "Spider-Man" foi lançado em 2018.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, "Bloodborne" foi lançado em 2015.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}Obrigado por usar o assistente de jogos PS4, {nome}! Até a próxima!{os.linesep}')
        return True  
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5')

def start():
    t
    print('Olá! Bem-vindo ao seu assistente de jogos PS4!')
    
    nome = input('Digite seu nome: ')
   
    email = input('Digite seu e-mail: ')
    
    while True:
        
        resposta = input(
            f'Sobre qual jogo gostaria de saber hoje?{os.linesep}[1] - Qual o ano de lançamento de "The Last of Us Part II"?{os.linesep}[2] - Qual o ano de lançamento de "Ghost of Tsushima"?{os.linesep}[3] - Qual o ano de lançamento de "Spider-Man"?{os.linesep}[4] - Qual o ano de lançamento de "Bloodborne"?{os.linesep}[5] - Sair{os.linesep}')
        
        
        if processar_resposta(resposta, nome):
            break  

if __name__ == '__main__':
    start()
