import subprocess
import sys
import threading
import tkinter as tk
from PIL import Image

from stt import recognize_from_microphone
from tts import convert_text_to_speech


class Assistant:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Displaying Avatar")
        file = "C:\\Users\\ss956\\Downloads\\ai_3.gif"
        info = Image.open(file)

        frames = info.n_frames  # number of frames

        photoimage_objects = []
        for i in range(frames):
            obj = tk.PhotoImage(file=file, format=f"gif -index {i}")
            photoimage_objects.append(obj)

        w = 100  # width for the Tk root
        h = 100  # height for the Tk root

        self.root.geometry('%dx%d+%d+%d' % (w, h, 1400, 500))
        gif_label = tk.Label(self.root, image="")
        gif_label.pack()

        # start.pack()

        stop = tk.Button(self.root, text="EXIT", command=self.stop_animation)
        stop.pack()
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.7)
        self.root.config(bg='#add123')

        # Create a transparent window
        self.root.wm_attributes('-transparentcolor', '#add123')
        self.root.overrideredirect(True)

        self.animation(root=self.root, frames=frames, gif_label=gif_label, photoimage_objects=photoimage_objects,
                       current_frame=0)

        def SaveLastClickPos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y

        def Dragging(event):
            x, y = event.x - lastClickX + self.root.winfo_x(), event.y - lastClickY + self.root.winfo_y()
            self.root.geometry("+%s+%s" % (x, y))

        self.root.bind('<Button-1>', SaveLastClickPos)
        self.root.bind('<B1-Motion>', Dragging)

        threading.Thread(target=self.run_ai_assistant).start()
        self.root.mainloop()

    def animation(self, root, frames, gif_label, photoimage_objects, current_frame=0):
        global loop
        image = photoimage_objects[current_frame]

        gif_label.configure(image=image)
        current_frame = current_frame + 1

        if current_frame == frames:
            current_frame = 0

        loop = root.after(50, lambda: self.animation(root, frames, gif_label, photoimage_objects, current_frame))

    def stop_animation(self):
        sys.exit()

    def run_ai_assistant(self):
        while True:
            spoken_phrase = recognize_from_microphone().lower()

            if 'hey, jarvis.' == spoken_phrase:
                jarvis_response_phrase = 'Hey, How Can I help you!'
            elif 'bye' in spoken_phrase:
                jarvis_response_phrase = 'Bye! see you later'
                convert_text_to_speech(jarvis_response_phrase)
                self.root.destroy()
                sys.exit(0)
            else:
                jarvis_response_phrase = spoken_phrase

            convert_text_to_speech(jarvis_response_phrase)


Assistant()
