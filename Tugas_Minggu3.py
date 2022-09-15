import asyncio
import time

get_time = time.time()

async def test():
    print("First Attempt")
    print(f"Finish in {time.time() - get_time} second\n")
    await asyncio.sleep(3) #Pausing For 3 Second
    print("Second Attempt")
    print(f"Finish in {time.time() - get_time} second\n")

async def get():
    await asyncio.gather(test())

asyncio.run(get())