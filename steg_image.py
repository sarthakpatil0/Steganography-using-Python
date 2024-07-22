import PIL.Image
import io

#### To Add Image ####
#img = PIL.Image.open('111.png')
#byte_arr = io.BytesIO()
#img.save(byte_arr, format='PNG')

#with open('cat.jpg', 'ab') as f:
#    f.write(byte_arr.getvalue())


#### To Extract the Image ####
with open('cat.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    new_img = PIL.Image.open(io.BytesIO(f.read()))
    new_img.save("new_image.png")
