from PyPDF4 import PdfFileWriter, PdfFileReader
import PyPDF4
  
  
PyPDF4.PdfFileReader('input.pdf')
  
  
def put_watermark(input_pdf, output_pdf, watermark):
    
    # reads the watermark pdf file through 
    # PdfFileReader
    watermark_instance = PdfFileReader(watermark)
      
    # fetches the respective page of 
    # watermark(1st page)
    watermark_page = watermark_instance.getPage(0)
      
    # reads the input pdf file
    pdf_reader = PdfFileReader(input_pdf)
      
    # It creates a pdf writer object for the
    # output file
    pdf_writer = PdfFileWriter()
  
    # iterates through the original pdf to
    # merge watermarks
    for page in range(pdf_reader.getNumPages()):
          
        page = pdf_reader.getPage(page)
          
        # will overlay the watermark_page on top 
        # of the current page.
        page.mergePage(watermark_page)
          
        # add that newly merged page to the
        # pdf_writer object.
        pdf_writer.addPage(page)
  
    with open(output_pdf, 'wb') as out:
          
        # writes to the respective output_pdf provided
        pdf_writer.write(out)
