import pdfkit
url = input('Enter the URL of the HTML: ')
pdf = input('Enter name of output pdf file without extension :')
pdfkit.from_url(url, pdf + '.pdf')
print("Done, The HTML url has been converted to PDF")
