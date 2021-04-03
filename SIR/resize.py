from PIL import Image
import os

size = (1120,840)
#size2 = (1138,655)

for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size)
        i.save(f'resized/{fn}_1120{fext}')

 #       i.thumbnail(size2)
  #      i.save(f'resized/{fn}_1138{fext}')
