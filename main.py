from tkinter import *
from tkinter import filedialog as fd
import watermark_tool
from tkinterdnd2 import *
from PIL import ImageTk, Image


def watermark_img():
    watermark_tool.add_watermark(file.get(), text.get(), size.get(), color.get())


def get_filename():
    filename = fd.askopenfilename()
    if filename:
        file.set(filename)
        show_img(filename)


def show_img(filename):
    # Image.thumbnail converts the image to a thumbnail
    image = Image.open(filename)
    image.thumbnail((320, 300), Image.LANCZOS)

    # now create the ImageTk PhotoImage:
    img = ImageTk.PhotoImage(image)
    in_frame.config(image=img)
    in_frame.photo = img


# start GUI for app
ws = TkinterDnD.Tk()
# base settings for the app display
ws.title("WaterMarkTool")
ws.geometry('350x600')
ws.config(bg='grey')

# folder path label and textbox
file = StringVar()  # set e_box as a string variable
Label(ws, text='Path of the Folder', bg='grey').pack(anchor=NW, padx=10)
e_box = Entry(ws, textvar=file, width=80)
e_box.pack(fill=X, padx=10)

# upload button for file path
button = Button(ws, text="Upload", command=get_filename)
button.pack(side=BOTTOM)

# watermark label and textbox
text = StringVar()  # set watermark_text as a string variable
Label(ws, text='Enter text to use as WaterMark', bg='grey').pack(anchor=NW, padx=10)
watermark_text = Entry(ws, textvar=text, width=80)
watermark_text.pack(fill=X, padx=10)

# font size label and entry
size = IntVar()  # set watermark_text as a string variable
Label(ws, text='Enter text size', bg='grey').pack(anchor=NW, padx=10)
watermark_text = Entry(ws, textvar=size, width=80)
watermark_text.pack(fill=X, padx=10)

# font color label and entry
color = StringVar()  # set watermark_text as a string variable
Label(ws, text='Enter color', bg='grey').pack(anchor=NW, padx=10)
watermark_text = Entry(ws, textvar=color, width=80)
watermark_text.pack(fill=X, padx=10)

# button for watermark
button = Button(ws, text="Add WaterMark", command=watermark_img)
button.pack(side=BOTTOM)

# in app preview
lframe = LabelFrame(ws, text="Preview", bg="grey")
lframe.pack(fill=BOTH, expand=True, padx=10, pady=10)

# show image
in_frame = Label(lframe, background="grey")
in_frame.pack()

ws.mainloop()  # keep GUI running
