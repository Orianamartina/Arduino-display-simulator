import serial
import numpy as np
import matplotlib.pyplot as plt

# Serial port setup (Change as needed)
port_name = "/dev/ttyACM0"  # Adjust for your system
baud_rate = 9600

ser = serial.Serial(port_name, baud_rate, timeout=1)


def read_image(width, height):
    while True:
        # Read 8-byte header
        header = b""
        while not header.endswith(b"IMGSTART"):
            header.endswith(ser.read())

        if header == b"IMGSTART":
            print("Receiving image data...")

            img_size = 1024  # 128x64 pixels → 1024 bytes (each byte = 8 pixels)
            img_data = bytearray()  # Use bytearray to collect bytes efficiently

            while len(img_data) < img_size:
                img_data.extend(ser.read(1))  # Read one byte at a time and add it

            print(f"Received {len(img_data)} bytes (Expected: {img_size})")

            if len(img_data) == img_size:
                # Convert to binary pixel matrix (1-bit per pixel)
                img_array = np.unpackbits(np.frombuffer(img_data, dtype=np.uint8))

                # Reshape into a 128x64 grid
                img_array = img_array.reshape((height, width))

                # Display the image
                plt.imshow(img_array, cmap="gray", vmin=0, vmax=1)
                plt.axis("off")
                plt.show()
            else:
                print(
                    f"Error: Received {len(img_data)} bytes instead of {img_size}. Check Arduino code."
                )


while True:
    read_image(128, 64)  # Expecting a 128x64 pixel image
