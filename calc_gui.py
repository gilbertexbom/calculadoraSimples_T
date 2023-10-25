# Interface gráfica da calculadora
from calculadora import *
import PySimpleGUI as psg

# psg.theme('DarkAmber')
psg.theme('BluePurple')

frame_layout = [
    [psg.Radio('Soma', 'rbgOpcoes', default=True, key='soma')],
    [psg.Radio('Subtração', 'rbgOpcoes', key='sub')]
]
layout = [
    [psg.Text('Num1: '), psg.InputText(key='n1'), psg.Frame('Opções: ', frame_layout)],
    [psg.Text('Num2: '), psg.InputText(key='n2')],
    [psg.Push(), psg.InputText(key='total', readonly=True, size=10), psg.Push()], # [psg.Text(key='total')],
    [psg.Push(), psg.Button('Calcular'), psg.Button('Limpar'), psg.Push()],
]

janela = psg.Window('Calculadora Simples - Soma', layout)

while True:
    eventos, valores = janela.read()

    if eventos == psg.WIN_CLOSED:
        break
    elif eventos == 'Limpar':
        janela['n1'].update('')
        janela['n2'].update('')
        janela['total'].update('')
        janela['n1'].set_focus(True)
        janela['soma'].update(True)
    else:
        if janela['soma'].get():
            janela['total'].update(soma(int(valores['n1']), int(valores['n2'])))
        else:
            janela['total'].update(sub(int(valores['n1']), int(valores['n2'])))
