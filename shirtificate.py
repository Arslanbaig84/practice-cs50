from fpdf import FPDF

name = input("Name: ")
#declaring pdf variable
pdf = FPDF()
#adding page
pdf.add_page()
#setting fond size for title
pdf.set_font("Times", "B", size=48)
#title
pdf.cell(0, 60, txt="CS50 Shirtificate", align="C")
#adding image
pdf.image("shirtificate.png", x=0, y=80)
#text on shirt
pdf.set_text_color(255, 255, 255)
pdf.text(x=50, y=150, txt=f"{name} took CS50")
#outputting file
pdf.output("shirtificate.pdf")
