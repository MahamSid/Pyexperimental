#img_viewer.py
#still need to read explanation + experiment with
#https://realpython.com/pysimplegui-python/


import PySimpleGUI as sg
import os.path

#Window layout: 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse,
    ],
    [
        sg.Listbox(
            values = [], enable_events = True, size=(40,20), key="-FILE LIST-"
            )
    ],
]

#Will only show name of file that was chosen
image_viewer_column = [
    [sg.Text("Choose image from list on left:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

#full layout =
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

#event loop
while True:
    event, values = window.read()
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png, .gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
                )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass
window.close()




