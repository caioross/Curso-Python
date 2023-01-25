from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as imgx

# Lista de nomes
nomes = ["João", "Maria", "thamy"]
evento = "Festa de Aniversário"
data = "20 de Janeiro de 2022"
local = "Rua das Flores, 123"

# Criando imagem do convite
for nome in nomes:
  img = Image.new("RGB", (600, 400), (255, 255, 255))
  draw = ImageDraw.Draw(img)

  # Adicionando informações do convite na imagem
  font_title = ImageFont.truetype("arial.ttf", 36)
  font_text = ImageFont.truetype("arial.ttf", 24)
  draw.text((50, 50), f"Convite para {nome}", (0, 0, 0), font=font_title)
  draw.text((50, 100), evento, (0, 0, 0), font=font_text)
  draw.text((50, 150), data, (0, 0, 0), font=font_text)
  draw.text((50, 200), local, (0, 0, 0), font=font_text)

  # Adicionando borda preta ao convite
  draw.rectangle([(45, 45), (555, 355)], outline=(0, 0, 0), width=5)

  # Salvando imagem do convite
  img.save(f"{nome}.jpg")
