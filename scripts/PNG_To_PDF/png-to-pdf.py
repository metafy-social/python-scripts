from PIL import Image

image1 = Image.open(r'png-to-pdf.png')
impdf = image1.convert('RGB')
impdf.save(r'png-to-pdf.pdf') # noqa