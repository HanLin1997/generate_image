from PIL import Image, ImageDraw, ImageFont
import random
import os
#import matplotlib.pyplot as plt

max_length = 20
gen_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def list_files_in_directory(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names

def generate_a_string():
    length = random.randint(1, max_length)
    string = ""
    for _ in range(length):
        string = string + random.choice(gen_char)
    return string

def generate_an_image(string):
    length = len(string)
    font_list = list_files_in_directory("./font")
    img_size = (20 + 25*length, 50)
    text_position = (random.randint(0,5*length), random.randint(0,20))
    image = Image.new("L", img_size)
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=text_position, text=string, fill=255, font=ImageFont.truetype(random.choice(font_list), 30))
    #image.save(f"./image/{string}.jpg")
    return image

def generate_images(num):
    with open("./image/label.txt", "w") as f:
        f.write("")
    for i in range(num):
        string = generate_a_string()
        image = generate_an_image(string)
        image.save(f"./image/{i}.jpg")
        with open("./image/label.txt", 'a') as f:
            f.write(string + '\n')

if __name__ == '__main__':
    generate_images(10)