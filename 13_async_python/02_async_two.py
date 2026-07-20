import asyncio
async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(brew("Masala chai"),
                         brew("Ginger chai"),
                         brew("Green chai"),)
asyncio.run(main())