from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

if __name__ == "__main__":
    bg = Image.open("out0.png") # The image to be cropped
    w, h = bg.size
    cropped = bg.crop((0, 150, w, h))
    new_im = trim(cropped)
    new_im.save("cropped.png")