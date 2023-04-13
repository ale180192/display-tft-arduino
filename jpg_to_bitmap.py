from PIL import Image

img = Image.open("images/frame_00_delay-0.04s.jpg")
img = img.convert(mode="1")
img = img.tobitmap("new_name")
print(img)