import serial
import time
import tkinter as tk


port_name = "/dev/ttyACM0"
ser = serial.Serial(port_name, 9600, timeout=1)
time.sleep(2)


# Setup the Tkinter window and canvas
root = tk.Tk()
root.title("Arduino Drawing Simulation")
canvas = tk.Canvas(root, width=320, height=240, bg="white")
canvas.pack()


def update_canvas():
    if ser.in_waiting:
        command = ser.readline().decode("utf-8").strip()
        if command:
            print("Received:", command)
            if command.upper() == "CLEAR":
                canvas.delete("all")
            elif command.startswith("DRAW"):
                parts = command.split()
                if len(parts) == 3:
                    try:
                        x, y = int(parts[1]), int(parts[2])
                        r = 5
                        canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")
                    except ValueError:
                        print("Invalid drawing coordinates")
    root.after(50, update_canvas)


update_canvas()
root.mainloop()
