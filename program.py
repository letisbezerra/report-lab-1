from reportlab.pdfgen import canvas 
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle
from reportlab.lib import colors 


fileName = 'pdfTable.pdf'

pdf = SimpleDocTemplate(
    fileName,
    pagesize = letter
)


data = [
    ['dadicated Hosting', 'VPS Hosting', 'Sharing Hosting', 'Reseller Hosting'],
    ['$200/month', '$100/month', '$50/month', '$20/month'],
    ['Free Domain', 'Free Domain', 'Free Domain', 'Free Domain'],
    ['2GB DDR2', '20GB Disco Space', 'Unlimited Email', 'Unlimited Email'],
]
tabela = Table(data) 


style= TableStyle([
    ('BACKGROUND', (0, 0), (3, 0), colors.green),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
    ('FONTSIZER', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
])
tabela.setStyle(style)


rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.burlywood
    else: 
        bc = colors.beige
    
    ts = TableStyle([
        ('BACKGROUND', (0, i), (-1, i), bc)
    ])
    tabela.setStyle(ts)

ts = TableStyle([
    ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ('LINEBEFORE', (2, 1), (2, -1), 2, colors.red),
    ('LINEABOVE', (0, 2), (-1, 2), 2, colors.green),
    ('GRID', (0, 0), (-1, -1), 2, colors.black),
    ])
tabela.setStyle(ts)


elems = []
elems.append(tabela)

pdf.build(elems)

