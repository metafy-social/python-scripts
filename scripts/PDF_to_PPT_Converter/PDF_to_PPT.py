import aspose.slides as slides
import aspose.pydrawing as drawing

with slides.Presentation() as presentation:  # Create presentation
    presentation.slides.remove_at(0) # this removes default slide from presentaion
    presentation.slides.add_from_pdf("path") # here path denotes the destination of the file you want to convert
    presentation.save("path", slides.export.SaveFormat.PPT) # here path denotes the destination of the converted file / the path where you want to save the converted PDF file