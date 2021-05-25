''' https://realpython.com/pysimplegui-python/ '''
# hello_psg.py
import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimple")], [sg.Button("OK")]]

#create window
window = sg.Window("Demo", layout)

#create an event loop
while True:
    event, values = window.read()
    #end prog if user closes window or presses OK
    if event == "OK" or event == sg.WIN_CLOSED:
        break


window.close()
