from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


pages = convert_from_path('C:\\Users\\david\\Downloads\\BorradorDeclaracion2019.pdf', dpi=500, output_folder='G:\\My Drive\\Contabilidad\\Gastos\\Expense_Receipts\\', fmt='jpg', single_file=False, output_file='BorradorDeclaracion2019')

#for page in pages:
    #page.save('G:\\My Drive\\Contabilidad\\Gastos\\Expense_Receipts\\out.jpg', 'JPEG')
