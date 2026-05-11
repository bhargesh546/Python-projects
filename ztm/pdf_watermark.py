import pypdf

reader = pypdf.PdfReader(open("super.pdf", "rb"))
watermark_reader = pypdf.PdfReader(open("water.pdf", "rb"))

writer = pypdf.PdfWriter()

watermark_page = watermark_reader.pages[0]

for page in reader.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as output_file:
    writer.write(output_file)

print("Watermark done!")