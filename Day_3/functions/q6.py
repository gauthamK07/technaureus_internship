import asyncio

async def api_call(name,delay):
    print(f"Waiting {delay} seconds to call API")
    await asyncio.sleep(delay)
    print(f"API call to {name} completed")
async def main():
    await asyncio.gather(
        api_call("API 1",1),
        api_call("API 2",2),
        api_call("API 3",3)
    )

asyncio.run(main())