import asyncio
import io

from pyppeteer import launch
from PIL import Image
import matplotlib.pyplot as plt

from wikipedia import get_revision_ids
from chunk_image import make_horizontal


async def screenshots(title):
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={title}'
    revision_list, ts_list = get_revision_ids(title)
    print(revision_list, ts_list)
    browser = await launch()
    page = await browser.newPage()
    for page_id, ts in zip(reversed(revision_list), reversed(ts_list)):
        print(ts)
        page_id_param = f'&oldid={page_id}'
        full_url = snapshot_url + page_id_param
        await page.goto(full_url)
        shot = await page.screenshot({'fullPage': True})
        image = make_horizontal(Image.open(io.BytesIO(shot)), max_chunk_size=2000)
        yield image, ts
    await browser.close()


figure, ax = plt.subplots()
plt.ion()


async def main(title):
    async for im, ts in screenshots(title):
        MAX_SIZE = (500, 500)
        im.thumbnail(MAX_SIZE)
        ax.clear()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.title(ts)
        plt.imshow(im)
        figure.canvas.draw()
        figure.canvas.flush_events()
        plt.show()


def play(title):
    asyncio.run(main(title=title))
