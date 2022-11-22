from PIL import Image
import glob

def reshape_image(image, size):
  iw, ih = image.size
  w, h = size
  scale = min(w/iw, h/ih)
  nw = int(iw * scale)
  nh = int(ih * scale)

  image = image.resize((nw, nh))
  new_image = Image.new('RGBA', size, (255, 255, 255, 0))
  new_image.paste(image, ((w - nw)//2, (h - nh)//2))
  return new_image

imgs = glob.glob('./default/*.png')

for i in imgs:
  image = Image.open(i)
  img = reshape_image(image, [80, 80])

  name = i.split('/')[::-1][0]
  img.save(f'./formatted/{name}')
  print(img.size)