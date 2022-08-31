import os
from PIL import Image

no = ["tabletop.png", "resize.py", "README.md", "sounds", "back.png"]

filename_map = {
    "h": "Hearts",
    "d": "Diamonds",
    "c": "Clubs",
    "s": "Spades",
}

value_map = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K",
}

images = os.listdir()

for i in images:
    if i.startswith('.'):
        continue
    if i not in no:
        print(i)
        value = int(i[1:-4])
        if value == 1 or value > 10:
            value = value_map[value]
        filename = filename_map[i[0:1]] + str(value) + ".png"
        print(filename)
        image = Image.open(i)
        print(image.size)
        image_resized = image.resize((80, 111))
        image_resized.save(filename)
        # os.system(f"convert {i} -resize 80x111\> {filename}")
