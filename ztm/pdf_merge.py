import sys, pypdf

inputs = sys.argv[1:]

def pdf_merge(pdf_lists):
    writer = pypdf.PdfWriter()

    for pdf in pdf_lists:
        print(pdf)
        writer.append(pdf)
    
    with open("super.pdf", "wb") as output_file:
        writer.write(output_file)

pdf_merge(inputs)