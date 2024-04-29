from fpdf import FPDF, Align
from PIL import Image, ImageDraw

# define PDF class that inherite FPDF class
class PDF(FPDF):

  def header(self):
    # setting font: font-family= Helvetica, style= bold, size = 45
    self.set_font("Helvetica", "", 45)

    # Printting text :
    self.cell(0, 22, "CS50 Shirtificate", align="c", center=True)

    # line break
    self.ln(40)


# define main fn
def main():
  # prompt user's name:
  name = input("Name: ").strip()
  name_text = f"{name} took CS50"

  # instantiate
  pdf = PDF(orientation="portrait", unit="mm", format="A4")
  pdf.add_page()

  # image manipulations using the Pillow library
  with Image.open("./shirtificate.png") as img:
    draw = ImageDraw.Draw(img)
    draw.text((110,180), name_text, font_size=28,  fill=(255,255,255), align="center")
    pdf.image(img, x=Align.C, w=pdf.eph*7/10)

  # create a PDF called shirtificate.pdf
  pdf.output("shirtificate.pdf")


if __name__ == "__main__":
  main()
