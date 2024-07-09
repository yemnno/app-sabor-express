import os

restaurantes_cadastrados = [{'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':False}, 
                            {'nome':'Praça', 'categoria':'Japonesa', 'ativo':True}]

def exibir_titulo():
      print("""
      
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
      
      """)

def opcao_invalida():
     print('Opção inválida!\n')
     input('\nDigite qualquer tecla para voltar ao menu principal: ')
     main()

def voltar_ao_menu_principal():
     input('\nDigite qualquer tecla para voltar ao menu principal ')
     main()

def exibir_subtitulo(texto):
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
     '''Essa função é responsável por cadastrar novos restautantes no sistema.
     
     Inputs:
     -nome do restaurante;
     -categoria;

     outputs:
     -adicionar o novo restaurante à lista de restaurantes cadastrados.
     
     '''
     exibir_subtitulo('Cadastro de novos restaurantes')

     nome_do_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
     categoria_do_restaurante = input(f'\nDigite a categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
     restaurantes_cadastrados.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
     
     voltar_ao_menu_principal()
 
def listar_restaurantes():
     exibir_subtitulo('Listando restaurantes cadastrados')

     print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

     for restaurante in restaurantes_cadastrados:
          nome_restaurante = restaurante['nome']
          categoria_restaurante = restaurante['categoria']
          restaurante_ativo = 'ativado' if restaurante['ativo'] else 'desativado'
          print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {restaurante_ativo}') 

     voltar_ao_menu_principal()


def alternar_estado_restaurante():
     exibir_subtitulo('Alterando estado do restaurante')
     nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
     restaurante_encontrado = False

     for restaurante in restaurantes_cadastrados:
          if nome_restaurante == restaurante['nome']:
               restaurante_encontrado = True
               restaurante['ativo'] = not restaurante['ativo']
               mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
               print(mensagem)
     if not restaurante_encontrado:
          print('O restaurante não foi encontrado.')
          
     voltar_ao_menu_principal()


def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Alterar status do restaurante')
      print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o programa!')

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            # opcao_escolhida = int(opcao_escolhida)

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()     
            else:
                  opcao_invalida()
      except:
           opcao_invalida()            


def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()    