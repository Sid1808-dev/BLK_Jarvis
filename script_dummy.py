import subprocess
import sys
import threading
import tkinter as tk
from PIL import Image

from stt import recognize_from_microphone
from tts import convert_text_to_speech


def generate_widget():
    root = tk.Tk()
    root.title("Displaying Avatar")
    file = "C:\\Users\\ss956\\Downloads\\ai_3.gif"
    info = Image.open(file)

    frames = info.n_frames  # number of frames

    photoimage_objects = []
    for i in range(frames):
        obj = tk.PhotoImage(file=file, format=f"gif -index {i}")
        photoimage_objects.append(obj)

    w = 100  # width for the Tk root
    h = 100  # height for the Tk root

    root.geometry('%dx%d+%d+%d' % (w, h, 1400, 500))
    gif_label = tk.Label(root, image="")
    gif_label.pack()

    # start.pack()

    stop = tk.Button(root, text="EXIT", command=stop_animation)
    stop.pack()
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.7)
    root.config(bg='#add123')

    # Create a transparent window
    root.wm_attributes('-transparentcolor', '#add123')
    root.overrideredirect(True)

    animation(root=root, frames=frames, gif_label=gif_label, photoimage_objects=photoimage_objects, current_frame=0)

    lastClickX = 0
    lastClickY = 0

    def SaveLastClickPos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+%s+%s" % (x, y))

    root.bind('<Button-1>', SaveLastClickPos)
    root.bind('<B1-Motion>', Dragging)

    threading.Thread(target=run_ai_assistant).start()
    root.mainloop()


def animation(root, frames, gif_label, photoimage_objects, current_frame=0):
    global loop
    image = photoimage_objects[current_frame]

    gif_label.configure(image=image)
    current_frame = current_frame + 1

    if current_frame == frames:
        current_frame = 0

    loop = root.after(50, lambda: animation(root, frames, gif_label, photoimage_objects, current_frame))


def stop_animation():
    sys.exit()


def run_ai_assistant():
    while True:
        spoken_phrase = recognize_from_microphone().lower()

        if 'hey, jarvis.' == spoken_phrase:
            jarvis_response_phrase = 'Hey, How Can I help you!'
        elif 'bye' in spoken_phrase:
            jarvis_response_phrase = 'Bye! see you later'
            convert_text_to_speech(jarvis_response_phrase)
            sys.exit()
        else:
            jarvis_response_phrase = spoken_phrase

        convert_text_to_speech(jarvis_response_phrase)


generate_widget()
