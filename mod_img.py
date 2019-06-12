from PIL import Image
import os


for root, dirs, files in os.walk('F:\Downloads\MyImages\ImageMiniLab'):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)

        img = Image.open(file_path)
        newImg = img.resize((int(img.width*0.4), int(img.height*0.4)), Image.BILINEAR)   #想调整的大小

        newImg.save(file_path)

