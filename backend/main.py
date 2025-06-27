from database import init_db
import asyncio

async def dermo():
    await init_db()

if __name__ == "__main__":
    asyncio.run(dermo())