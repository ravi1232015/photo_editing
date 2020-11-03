from PIL import Image, ImageEnhance, ImageFilter
import os
img1 = Image.open('DSC_0279.JPG')
img1.save('DSC_0279.pdf')
img1.show()
MAX_SIZE = (100000,800000)
img1.thumbnail(MAX_SIZE)
#img1.Backgrond('C:/Users/HP/Pictures/Screenshots/Screenshot (30).png')
img1.save('DSC_0279.jpg')

for item in os.listdir():
        if item.endswith('.jpg'):
                img1 = Image.open(item)
                filename,extension = os.path.splitext(item)
                img1.save(f'{filename}.jpg')
                

#img1 = Image.open('DSC_0279.jpg')
enhancer = ImageEnhance.Sharpness(img1)
#enhancer = ImageEnhance.color(img1)
enhancer.enhance(2).save('DSC_0279edited.jpg')

img1 = Image.open('DSC_0279.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(5).save('DSC_0279edited.jpg')


img1 = Image.open('DSC_0279.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(5).save('DSC_0279edited.jpg')

img1 = Image.open('DSC_0279.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(5).save('DSC_0279edited.jpg')

img1 = Image.open('DSC_0279.jpg')
img1.filter(ImageFilter.GaussianBlur(radius=2)).save('DSC_0279.jpgedited.jpg')
