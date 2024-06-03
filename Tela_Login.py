from PySimpleGUI import PySimpleGUI as sg

sg.theme('Dark Green 7')
layout = [
        [sg.Text('Usuário'), sg.Input(key= 'usuario', size=(30,1))],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(31,1))],
        [sg.Listbox(values=[], key='ARQUIVOS', size=(40, 6))],
        [sg.Checkbox('Salvar o login')],
        [sg.Button('Entrar')]
]

# janela #
janela = sg.Window('Tela de Login', layout)
# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'leandro' and valores['senha'] == '1234':
            print('Bem-vindo Leandro')