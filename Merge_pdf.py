from pypdf import PdfWriter  # <-- Changed this line

# 1. Create a Writer object (instead of PdfMerger)
merger = PdfWriter()  # <-- Changed this line

pdf_files = ['class 11.pdf', 'class 12.pdf']

print("Merging Files...")

for pdf in pdf_files:
    merger.append(pdf)

merger.write("Physics_Notes.pdf")
merger.close()

print("Merged successfully!")