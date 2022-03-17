import os
from PIL import Image
from generateAnnotations import generateAnnotations

__dirname__ = os.path.dirname(os.path.abspath(__file__))
__basename__ = os.path.basename(__dirname__)

JPEGImages_dir = os.path.join(__dirname__, "JPEGImages")
Annotations_dir = os.path.join(__dirname__, "Annotations")
ImageSets_dir = os.path.join(__dirname__, "ImageSets/Main")
model_images_dir = os.path.join(__dirname__, "images")

labels_file = open('labels.txt', 'a')
trainval_file = open(os.path.join(ImageSets_dir, "trainval.txt"), 'a')

print("=============================")
print("Configuration ~\n")

if (os.path.isdir(JPEGImages_dir)):
    pass
else:
    print("Making JPEGImages Folder \n")
    os.mkdir(JPEGImages_dir)

if (os.path.isdir(Annotations_dir)):
    pass
else:
    print("Making Annotations Folder \n")
    os.mkdir(Annotations_dir)


if (os.path.isdir(ImageSets_dir)):
    pass
else:
    print("Making ImageSets Folder \n")
    print(ImageSets_dir)
    os.mkdir(os.path.join(__dirname__, "ImageSets"))
    os.mkdir(ImageSets_dir)

print("============================= \n")

print("Scanning ~ \n")

# images > (folder)
for folder in os.scandir(model_images_dir):
    if folder.is_dir:
        objectname = folder.name
        model_dir = os.path.join(model_images_dir, folder.name)

        labels_file.write(f"{folder.name}\n")

        """
        when getting an image;
        - it should save it on JPEGImages Folder
        - it should generates xml file in Annotations folder
        - 
        """
        for file in os.scandir(model_dir):
            # when ferrubg 
            if file.is_file:

                filename = f"{folder.name}-{file.name}"

                # a filename without the extension (jpg), used for generating Annotation's xml file
                imagename = filename.replace('.jpg', '')

                image = Image.open(os.path.join(model_dir, file.name))
                
                # writing Annotation's XML File
                image_annotations_file = open(os.path.join(Annotations_dir, f"{imagename}.xml"), 'a')
                image_annotations_file.write(generateAnnotations(filename, __basename__, objectname, image.size, (0, image.size[1]), (0,  image.size[0])))

                # insert imagename onto trainval.txt
                
                trainval_file.write(imagename+'\n')

                # print image
                print(os.path.join(JPEGImages_dir, filename))

                # JPEGImage = image.convert('RGB')
                # JPEGImage.save(os.path.join(JPEGImages_dir, filename))
                image.save(os.path.join(JPEGImages_dir, filename))

trainval_file.close()
labels_file.close()