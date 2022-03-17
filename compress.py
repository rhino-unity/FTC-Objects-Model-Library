import gzip
from pickletools import optimize
import shutil
import os
from PIL import Image

__dirname__ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
__currentdir__ = os.path.dirname(os.path.abspath(__file__))
__imagecompresseddir__ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_compressed')

try:
    os.mkdir('image_compressed')
except:
    pass

for folder in os.scandir(__dirname__):
    pass
    if folder.is_dir:
        foldername = os.path.join(__imagecompresseddir__, folder.name)
        
        try:
            os.remove(foldername)
        except:
            pass

        os.mkdir(foldername)
        for file in os.scandir(os.path.join(__dirname__, folder.name)):
            if file.is_file:
                print(file.name)
                image = Image.open(os.path.join(__dirname__, folder.name+f'/{file.name}'))
                image.save(os.path.join(foldername, f"{file.name.replace('.png', '')}.png"),
                 optimize=True,
                 quality = 6)

                
