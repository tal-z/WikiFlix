import asyncio
import io

from pyppeteer import launch
from PIL import Image
import matplotlib.pyplot as plt

from wikipedia import get_revision_ids


async def screenshots(title):
    snapshot_url = f'https://en.wikipedia.org/w/index.php?title={title}'
    revision_list = get_revision_ids(title)
    browser = await launch()
    page = await browser.newPage()
    for page_id in reversed(revision_list):
        page_id_param = f'&oldid={page_id}'
        full_url = snapshot_url + page_id_param
        await page.goto(full_url)
        shot = await page.screenshot({'fullPage': True})
        image = Image.open(io.BytesIO(shot))
        yield image
    await browser.close()


figure, ax = plt.subplots()
plt.ion()

async def main(title):
    count = 0
    async for i in screenshots(title):
        print(count)
        count += 1
        MAX_SIZE = (500, 500)
        i.thumbnail(MAX_SIZE)
        ax.clear()
        plt.imshow(i)
        figure.canvas.draw()
        figure.canvas.flush_events()
        plt.show()

title = 'Little_Red_Lighthouse'
asyncio.run(main(title=title))
