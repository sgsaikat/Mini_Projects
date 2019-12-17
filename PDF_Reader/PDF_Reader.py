import PyPDF2
from PIL import Image

pdfFileObj = open('Plastic_EVE2020.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
img_num = 0

# Credit - https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
def save_image(pageObj):
    global img_num
    xObject = pageObj['/Resources']['/XObject'].getObject()
    
    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            
            try:
                data = xObject[obj]._data
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"

                if xObject[obj]['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode, size, data)
                    img.save("images/" + str(img_num) + ".png")
                elif xObject[obj]['/Filter'] == '/DCTDecode':
                    with open("images/" + str(img_num) + ".jpg", "wb") as img:
                        img.write(data)
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    with open("images/" + str(img_num) + ".jp2", "wb") as img:
                        img.write(data)
            except ValueError as err:
                print(obj)
                continue
            
            img_num += 1

with open('pdf_txt.txt', 'w', encoding='utf-8') as f:
    for page in range(pdfReader.numPages):
        page_break = ("\n" + ">"*30 + " Page No: " + str(page) + " " + "<"*30 + "\n")
        f.write(page_break)
        pageObj = pdfReader.getPage(page)
        f.write(pageObj.extractText())
        save_image(pageObj)