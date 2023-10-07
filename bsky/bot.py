import urllib.request
from pdf2image import convert_from_path
import random
import os
import PyPDF2
from atproto import Client
from PIL import Image, ImageChops
from io import BytesIO






def trim(im):
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
                return im.crop(bbox)

def crop():
        n = 0

        for file in os.listdir('.'):
                if file.endswith('.jpeg'):
                        bg = Image.open(file) # The image to be cropped
                        w, h = bg.size
                        cropped = bg.crop((0, 150, w, h))
                        new_im = trim(cropped)
                        cropped_name = "cropped{}.jpeg".format(n)
                        new_im.save(cropped_name)
                        os.remove(file)


def convert():
        n = 0

        pages = convert_from_path('pdf.pdf', 100)
        for page in pages:
                filename = 'out{}.jpeg'.format(n)
                page.save(filename, 'JPEG')
                n = n + 1


def scrape():
        global art_url, date

        article = random.randrange(1, 100)
        day = random.randrange(1, 30)
        month = random.randrange(1, 12)
        year = random.randrange(1897, 1979)
        url = "https://www.nli.org.il/en/newspapers/?a=is&oid=frw{}{}{}-01.2.{}&type=nlilogicalsectionpdf&e=-------en-20--1--img-txIN%7ctxTI--------------1".format(year, format(month, '02d'), format(day, '02d'), article )
        art_url = "https://www.nli.org.il/en/newspapers/frw/{}/{}/{}/01/article/{}".format(year, format(month, '02d'), format(day, '02d'), article )
        date = "{}/{}/{}".format(month, day, year)
        print(date)

        for file in os.listdir('.'):
                if file.endswith('.jpeg'):
                        os.remove(file)
        for file in os.listdir('.'):
                if file.endswith('.pdf'):
                        os.remove(file)

        print(url)

        urllib.request.urlretrieve(url, "pdf.pdf")

        try:
                PyPDF2.PdfReader(open("pdf.pdf", "rb"))
        except PyPDF2.errors.PdfReadError:
                scrape()
        else:
                convert()


scrape()
crop()

if os.path.getsize('cropped0.jpeg') > 976000:
        im1 = Image.open('cropped0.jpeg')
        buffer = BytesIO()
        im1.save(buffer, "JPEG", quality=10)

status = date + "\n\n" + art_url

client = Client()
client.login('', '')

with open('cropped0.jpeg', 'rb') as f:
        img_data = f.read()
        #client.send_image(text=status, image=img_data, image_alt=date)
#post_result = api.update_status(status, media_ids=media_ids)
print(date)