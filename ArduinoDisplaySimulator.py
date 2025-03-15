import tkinter as tk

import numpy as np
import serial
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Bitmap Viewer")
canvas = tk.Label(root)
canvas.pack()

port_name = "/dev/ttyACM0"
baud_rate = 9600

ser = serial.Serial(port_name, baud_rate, timeout=1)
width, height = 128, 64


def update_image(img_data, img_size, width, height):
    if len(img_data) == img_size:
        img_array = np.unpackbits(np.frombuffer(img_data, dtype=np.uint8))
        img_array = img_array.reshape((height, width))
        img_array = np.flipud(img_array)

        img = Image.fromarray((img_array * 255).astype(np.uint8))

        img_tk = ImageTk.PhotoImage(image=img)
        canvas.config(image=img_tk)
        canvas.image = img_tk

    else:
        print(f"Error: Received {len(img_data)} bytes instead of {img_size}")


def read_image():
    while True:
        # Read 8-byte header
        header = ser.read(8)

        if header == b"IMGSTART":
            print("Receiving image data...")

            img_size = 1024
            img_data = bytearray()

            while len(img_data) < img_size:
                byte = ser.read()
                img_data.extend(byte)

            print(f"Received {len(img_data)} bytes (Expected: {img_size})")

            update_image(img_data, img_size, width, height)
            root.after(2, read_image)
            break


read_image()
root.mainloop()
