# hello_psg.py
#import client 

import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [[sg.Text("Hello",text_color= "red",justification="middle",pad=(100,100),font=(100),auto_size_text= True)],
        
        [sg.Button("OK",button_color="green"),]
        ]

# Create the window
window = sg.Window("Demo", layout,resizable=True)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()