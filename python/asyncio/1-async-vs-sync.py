# Async version
import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print(f"executed in {elapsed:0.2f} seconds.")

# Sync version
def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

s = time.perf_counter()
main()
elapsed = time.perf_counter() - s
print(f"executed in {elapsed:0.2f} seconds.")
