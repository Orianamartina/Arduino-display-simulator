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
    print(f"Extracted {len(pixel_data)} bytes (Expected: {SIZE[0] * SIZE[1]})")


if __name__ == "__main__":
    bmp_path = "./rdr2.bmp"
    h_path = "./rdr2.h"

    image = Image.open("./red-dead-redemption-2-review_81k9.1024.webp")
    image = image.resize(SIZE)

    image = image.convert("1")

    image.save(bmp_path, format="BMP")
    bmp_to_header(bmp_path, h_path)
