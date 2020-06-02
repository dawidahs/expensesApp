from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

pages = convert_from_path('C:\\Users\\david\\Downloads\\BorradorDeclaracion2019.pdf', dpi=500, single_file=False)

for page in pages:
    page.save('G:\\My Drive\\Contabilidad\\Gastos\\Expense_Receipts\\out.jpg', 'JPEG')