# from print_ascii import total_colors
from PIL import Image
import numpy as np
# import cProfile

def total_colors_getpixel(img: Image) -> int:
    """
    Количество цветов в изображении, ручная реализация
    """
    total_color = set()
    for x in range(img.width):
        for y in range(img.height):
            total_color.add(img.getpixel((x, y)))

    return len(total_color)


def total_colors_dict(img: Image):
    """
    Количество цветов в изображении, Counter
    """
    pass
    # return len(total_color)


def total_colors_np_unique(image):
    # rgb = np.array(image).astype(np.uint32).reshape((-1, 3))
    rgb = np.array(image).astype(np.uint32)
    if rgb.shape[2] == 4:   # есть альфа-канал
        rgb = rgb[:, :, 0:3]
    rgb = rgb.reshape((-1, 3))
    rgb = (rgb[:, 0] << 16 |
           rgb[:, 1] << 8 |
           rgb[:, 2])
    # fraction = 0.05
    # size = int(rgb.size * fraction)
    # rgb = np.random.choice(rgb, size=size, replace=False)
    unique, counts = np.unique(rgb, return_counts=True)
    return len(unique)


if __name__ == '__main__':
    image_name = r"d:\dev\data\get_background_color.png"
    image = Image.open(image_name)
    print(total_colors_getpixel(image))
    # print(total_colors_dict(image))
    print(total_colors_np_unique(image))
