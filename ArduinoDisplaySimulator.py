import matplotlib.pyplot as plt
import numpy as np
import serial

# Serial port setup (Change as needed)
port_name = "/dev/ttyACM0"  # Adjust for your system
baud_rate = 9600

ser = serial.Serial(port_name, baud_rate, timeout=1)


def read_image(width, height):
    while True:
        # Read 8-byte header
        header = ser.read(8)

        if header == b"IMGSTART":
            print("Receiving image data...")

            img_size = 1024
            img_data = bytearray()

            while len(img_data) < img_size:
                byte = ser.read(1)
                img_data.extend(byte)

            print(f"Received {len(img_data)} bytes (Expected: {img_size})")

            if len(img_data) == img_size:
                img_array = np.unpackbits(np.frombuffer(img_data, dtype=np.uint8))
                print(img_array)
                img_array = img_array.reshape((height, width))
                img_array = np.flipud(img_array)

                # Display the image
                plt.imshow(img_array, cmap="gray", vmin=0, vmax=1)
                plt.axis("off")
                plt.show()
            else:
                print(
                    f"Error: Received {len(img_data)} bytes instead of {img_size}. Check Arduino code."
                )


while True:
    read_image(128, 64)
