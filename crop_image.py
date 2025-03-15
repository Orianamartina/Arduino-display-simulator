from PIL import Image


def split_image(image_path, margin=10):
    img = Image.open(image_path)
    width, height = img.size

    img_cropped = img.crop((margin, margin - 5, width - margin, height - margin))
    img_cropped.show()
    new_width, new_height = img_cropped.size

    # Dividir en 12 partes (3 columnas x 4 filas)
    cols, rows = 6, 2
    cell_width = new_width // cols
    cell_height = new_height // rows

    images = []
    for row in range(rows):
        for col in range(cols):
            left = col * cell_width
            upper = row * cell_height
            right = left + cell_width
            lower = upper + cell_height
            cropped = img_cropped.crop((left, upper, right, lower))
            images.append(cropped)

    return images


image_path = "./horse-run-cycle-silhouette-animation-260nw-712211197.webp"

cropped_images = split_image(image_path, margin=20)

for idx, img in enumerate(cropped_images):
    img.save(f"recorte_{idx+1}.png")

# cropped_images[0].show()
