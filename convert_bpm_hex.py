import sys

from PIL import Image

SIZE = (128, 64)


def bmp_to_header(bmp_file, header_file, var_name="bitmap_data"):
    with open(bmp_file, "rb") as f:
        bmp_data = f.read()

    pixel_data_offset = int.from_bytes(bmp_data[10:14], byteorder="little")
    pixel_data = bmp_data[pixel_data_offset:]

    hex_values = ", ".join(f"0x{byte:02X}" for byte in pixel_data)

    with open(header_file, "w") as f:
        f.write(f"#ifndef {var_name.upper()}_H\n")
        f.write(f"#define {var_name.upper()}_H\n\n")
        f.write(
            f"const unsigned char {var_name}[] PROGMEM = {{\n    {hex_values}\n}};\n\n"
        )
        f.write(f"#endif // {var_name.upper()}_H\n")

    print(f"Header file '{header_file}' generated successfully.")


if __name__ == "__main__":
    bmp_path = "./recortes/"
    h_path = "./arduino/main/recortes/"

    for i in range(12):
        image = Image.open(f"./recorte_{i+1}.png")
        image = image.resize(SIZE)

        image = image.convert("1")

        image.save(f"{bmp_path}/recorte_{i+1}.bmp", format="BMP")
        bmp_to_header(f"{bmp_path}/recorte_{i+1}.bmp", f"{h_path}/recorte_{i+1}.h")
