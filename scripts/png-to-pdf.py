from PIL import Image

image1 = Image.open(r'C:\Users\user\Downloads\png-to-pdf.png')
impdf = image1.convert('RGB')
impdf.save(r'C:\Users\user\Downloads\png-to-pdf.pdf') # noqa