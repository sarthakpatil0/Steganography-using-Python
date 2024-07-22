#with open('imag.jpeg', 'ab') as f:
#    f.write(b"Hello World")


with open('imag.jpeg', 'rb') as f:
    text = f.read()
    offset = text.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    print(f.read())
