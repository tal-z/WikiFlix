import asyncio
import copy
import io

from pyppeteer import launch
from PIL import Image
import matplotlib.pyplot as plt

from wikipedia import get_revision_ids


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
        image = Image.open(io.BytesIO(shot))
        yield image, ts
    await browser.close()


figure, ax = plt.subplots()
plt.ion()



async def main(title):
    count = 0
    async for i, ts in screenshots(title):
        print(count, ts)
        count += 1
        print(i.size)
        MAX_SIZE = (500, 500)
        i.thumbnail(MAX_SIZE)
        print(i.size)
        ax.clear()
        plt.title(ts)
        plt.imshow(i)
        figure.canvas.draw()
        figure.canvas.flush_events()
        plt.show()

title = 'Little Red Lighthouse'
asyncio.run(main(title=title))
