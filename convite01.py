# Importando bibliotecas necessárias
from PIL import Image, ImageDraw, ImageFont
from google.colab import files

# Informações do convite
nome = "João da Silva"
evento = "Festa de Aniversário"
data = "20 de Janeiro de 2022"
local = "Rua das Flores, 123"

# Criando imagem do convite
img = Image.new("RGB", (600, 400), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Adicionando informações do convite na imagem
font = ImageFont.truetype("arial.ttf", 36)
draw.text((50, 50), f"Convite para {nome}", (0, 0, 0), font=font)
draw.text((50, 100), evento, (0, 0, 0), font=font)
draw.text((50, 150), data, (0, 0, 0), font=font)
draw.text((50, 200), local, (0, 0, 0), font=font)

# Salvando imagem do convite
img.save(f"convite_{nome}.jpg")

from IPython.display import Image

# Exibindo a imagem
Image(filename='convite_João da Silva.jpg')
