import pypdf

with open("dummy1.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    writer = pypdf.PdfWriter()

    page = reader.pages[0]

    page.rotate(90)

    writer.add_page(page)

    with open("rotated.pdf", "wb") as output_file:
        writer.write(output_file)

    # print(len(reader.pages))
    # print(reader.pages[0])