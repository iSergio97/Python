from mapa import classMap
from PIL import Image

image = Image.open("mapa.png")
image.show()

classMap()

# print("Pre coloreado")
# print("\033[0;31;40m Red exception")
# print("\033[0;31;41m Red exception")
# print("\033[0;31;42m Red exception")
# print("\033[0;31;43m Red exception")
# print("\033[0;31;44m Red exception")
# print("\033[0;31;45m Red exception")
# print("\033[0;31;46m Red exception")
# print("\033[0;31;47m Red exception")
# print("\033[94m Color especial")
# print("\033[0m")
# print("Post coloreado")