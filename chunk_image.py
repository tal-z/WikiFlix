from PIL import Image

im = Image.open(r"C:\Users\PC\Pictures\Untitled.png")

im.show()

def make_rectangular(image):
    # use floor division to get number of chunks
    # use modulus to get size of remainder
    # the remainder counts as an extra chunk.
    # always do it as the last step, even when there are "no chunks" per floor division. in that case, it is the height
    max_chunk_size = 4000
    chunks = image.height // max_chunk_size
    remainder = image.height % max_chunk_size

    cropped = None

    if chunks or remainder:
        for chunk in range(chunks):
            start = chunk* max_chunk_size
            end = start+max_chunk_size
            print(start, end)
            if not cropped:
                cropped = image.crop((0, start, image.width, end))
            else:
                cropped.paste(image.crop((0, start, image.width, end)), box=(cropped.width, 0))
            cropped.show()

        if remainder:
            cropped = image.crop((0, image.height-remainder, image.width, image.height))
            cropped.show()




make_rectangular(im)
