"""
# Profiler Research v 1.0
"""
from PIL import Image


def total_colors_v_1_0(img: Image) -> int:
    total_color = set()
    for x in range(img.width):
        for y in range(img.height):
            total_color.add(img.getpixel((x, y)))

    return len(total_color)


if __name__ == '__main__':
    image_name = "data/get_background_color.png"
    image = Image.open(image_name)
    print(f"{total_colors_v_1_0(image)=} colors")
