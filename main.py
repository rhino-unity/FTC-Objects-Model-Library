import os
from PIL import Image
from generateAnnotations import generateAnnotations
from typing import Tuple
from copy import copy

__dirname__ = os.path.dirname(os.path.abspath(__file__))
__basename__ = os.path.basename(__dirname__)

JPEGImages_dir = os.path.join(__dirname__, "JPEGImages")
Annotations_dir = os.path.join(__dirname__, "Annotations")
ImageSets_dir = os.path.join(__dirname__, "ImageSets/Main")
model_images_dir = os.path.join(__dirname__, "FTC-Images")

labels_file = open('labels.txt', 'w')

print("=============================")
print("Configuration ~\n")

dirs = os.listdir()

for rd in ['JPEGImages', 'Annotations', 'ImageSets']:
    if rd not in dirs:
        os.mkdir(rd)
        if rd == 'ImageSets':
            os.mkdir('ImageSets/Main')

trainval_file = open(os.path.join(ImageSets_dir, "trainval.txt"), 'a')


print("============================= \n")

print("Scanning ~ \n")

class xml:
    _xml_string = open("annotation_xml.xml").read()

    @staticmethod
    def render(
            filename:str, 
            folder:str, 
            im_name: str, 
            im_size:Tuple[int, int]=(512, 512), 
            im_min:Tuple[int, int]=(0,0), 
            im_max:Tuple[int, int]=(512, 512)
        ):
            gen_xml = copy(xml._xml_string)
            gen_xml = gen_xml.replace(r'{%FILENAME%}', filename)
            gen_xml = gen_xml.replace(r'{%FOLDER%}', folder)
            gen_xml = gen_xml.replace(r'{%OBJ_NAME%}', im_name)
            gen_xml = gen_xml.replace(r'{%IMG_X%}', str(im_size[0]))
            gen_xml = gen_xml.replace(r'{%IMG_Y%}', str(im_size[1]))
            gen_xml = gen_xml.replace(r'{%MIN_X%}', str(im_min[0]))
            gen_xml = gen_xml.replace(r'{%MIN_Y%}', str(im_min[1]))
            gen_xml = gen_xml.replace(r'{%MAX_X%}', str(im_max[0]))
            gen_xml = gen_xml.replace(r'{%MAX_Y%}', str(im_max[1]))
            return gen_xml

# images > (folder)
models = []

for folder in os.scandir(model_images_dir):
    if folder.is_dir:
        objectname = folder.name
        model_dir = os.path.join(model_images_dir, objectname)
        models.append(folder.name)

        print(f"Scan {folder.name} model..")

        """
        when getting an image;
        - it should save it on JPEGImages Folder
        - it should generates xml file in Annotations folder
        - 
        """
        try:
            for file in os.scandir(model_dir):
                # when ferrubg 
                if file.is_file:
                    
                    filename = f"{folder.name}-{file.name}"
                    # print(filename)
                    if filename.startswith('.'):
                        continue

                    # a filename without the extension (jpg), used for generating Annotation's xml file
                    imagename = filename.replace('.jpg', '')

                    image = Image.open(os.path.join(model_dir, file.name))
                    

                    # writing Annotation's XML File
                    # image_annotations_file = open(os.path.join(Annotations_dir, f"{imagename}.xml"), 'a')
                    # image_annotations_file.write(generateAnnotations(filename, __basename__, objectname, image.size, (0, image.size[1]), (0,  image.size[0])))

                    # insert imagename onto trainval.txt
                    
                    # trainval_file.write(imagename+'\n')

                    # print image
                    # print(os.path.join(JPEGImages_dir, filename))

                    # JPEGImage = image.convert('RGB')
                    # JPEGImage.save(os.path.join(JPEGImages_dir, filename))
                    image.save(os.path.join(JPEGImages_dir, filename))
        except:
            pass

for model in models:
    labels_file.write("\n".join(model))

print('Begin XML generator')
vals = []

for fn in list(sorted(os.listdir('JPEGImages'))):
    fn_no_ext = fn.split(".")[0]
    with open(f'Annotations/{fn_no_ext}.xml', 'w') as f:
        image = Image.open(os.path.join(JPEGImages_dir, fn))

        print(image.size)

        f.write(xml.render(fn, __basename__, fn.split('-')[0], im_size=(image.size[0], image.size[1]), im_min=(50, 50), im_max=(image.size[0]-100, image.size[1]-100)))
    vals.append(fn_no_ext)
    print(f'\r{fn}', end='')

print('\nMaking txt files')

with open('ImageSets/Main/train.txt', 'w') as f:
    f.write('\n'.join(vals))


print("Done!")

trainval_file.close()
labels_file.close()

# print(list(sorted(os.scandir(model_dir))))