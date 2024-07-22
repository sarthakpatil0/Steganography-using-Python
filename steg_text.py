#### To Add Hide Text in the Image ####
#with open('imag.jpeg', 'ab') as f:
#    f.write(b"Hello World")


#### To Extract the Text from the Image ####
with open('imag.jpeg', 'rb') as f:
    text = f.read()
    offset = text.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    print(f.read())
