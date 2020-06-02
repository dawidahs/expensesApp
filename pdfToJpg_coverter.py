from pdf2image import convert_from_path

pages = convert_from_path('C:\Users\david\Downloads\1_Personal+Statement+Bulk+Print+1590664876968.pdf', 500)

for page in pages:
    page.save('out.jpg', 'JPEG')