# Interface gráfica da calculadora
from calculadora import soma
import PySimpleGUI as psg

layout = [
    [psg.Text('Num1: '), psg.InputText(key='n1')],
    [psg.Text('Num2: '), psg.InputText(key='n2')],
    [psg.Text(key='total')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
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
    else:
        janela['total'].update(soma(int(valores['n1']), int(valores['n2'])))
