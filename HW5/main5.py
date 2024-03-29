import time
import aiohttp
import asyncio
import os

async def download_image(session, url, filename):
    async with session.get(url) as response:
        if response.status == 200:
            with open(filename, 'wb') as f:
                f.write(await response.read())


async def download_images(img_num, output_folder):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(img_num):
            image_url = f"https://picsum.photos/1000/1000"
            filename = output_folder + f"/image_{i}.jpg"
            tasks.append(asyncio.create_task(download_image(session, image_url, filename)))
        await asyncio.gather(*tasks)

async def main():
    n = 100
    output_folder = "artifacts/images"  #

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    await download_images(n, output_folder)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time - start_time)