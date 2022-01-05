from PIL import Image
import pdb


im = Image.open(r"C:\Users\PC\PycharmProjects\SocketIOPlaytime\frames\frame42.jpg")

#im.show()
print(im.height, im.width)

def make_rectangular(image):
    # use floor division to get number of chunks
    # use modulus to get size of remainder
    # the remainder counts as an extra chunk.
    # always do it as the last step, even when there are "no chunks" per floor division. in that case, it is the height
    max_chunk_size = 400
    chunks = image.height // max_chunk_size
    remainder = image.height % max_chunk_size

    cropped = None
    """
    if the height is so long that it exceeds...scale it down and go from there. 
    """


    new_image = Image.new(mode='RGB', size=(image.width * (chunks+1), max_chunk_size))

    if chunks or remainder:
        for chunk in range(chunks):
            start = chunk * max_chunk_size
            end = start+max_chunk_size
            print(start, end)
            cropped = image.crop((0, start, image.width, end))
            new_image.paste(cropped, box=(image.width * chunk, 0))

        if remainder:
            cropped = image.crop((0, image.height-remainder, image.width, image.height))
            new_image.paste(cropped, box=(image.width * chunks, 0))
            new_image.show()




make_rectangular(im)
