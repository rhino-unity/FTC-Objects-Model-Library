from turtle import width


def generateAnnotations(filename, foldername, objectname, size, yminmax=(1080, 1080), xminmax=(1080, 1080)):
    content = f"""<annotation>
    <filename>{filename}</filename>
    <folder>{foldername}</folder>
    <source>
        <database>{foldername}</database>
        <annotation>custom</annotation>
        <image>custom</image>
    </source>
    <size>
        <width>{size[0]}</width>
        <height>{size[1]}</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>{objectname}</name>
        <pose>unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>0</xmin>
            <ymin>0</ymin>
            <xmax>{xminmax[1]}</xmax>
            <ymax>{yminmax[1]}</ymax>
        </bndbox>
    </object>
</annotation>
    """
    return content