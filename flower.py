from PIL import Image
import os
fin = 'D:/gsj/研究生涯/杂七杂八/flower_photos/flower_photos/tulips'
fout = 'D:/gsj/研究生涯/杂七杂八/flower_photos/test/test4'
os.mkdir(fout)
for file in os.listdir(fin):
    file_fullname = fin + '/' +file
    img = Image.open(file_fullname)
    a = [0, 0, 299, 299]
    box = (a)
    roi = img.crop(box)
    if fout not in os.listdir('D:/'):

        out_path = fout + '/' + file
        roi.save(out_path)