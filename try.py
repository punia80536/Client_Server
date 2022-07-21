import PySimpleGUI as sg

def main():
    layout = [
        [sg.Button('Keep on Top'), sg.Button('Not Keep on Top')]
    ]
    window = sg.Window("Title", layout, keep_on_top=True, finalize=True)
    setting = {'Keep on Top':1, 'Not Keep on Top':0}
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WINDOW_CLOSED:
            break
        if event in setting:
            window.TKroot.wm_attributes("-topmost", setting[event])

    window.close()

if __name__ == '__main__':
    main()