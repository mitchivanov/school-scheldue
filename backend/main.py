from database import init_db
# Импортируем все модели чтобы они зарегистрировались в Base
from models import model
import asyncio

async def dermo():
    await init_db()
    print("Таблицы успешно созданы!")

if __name__ == "__main__":
    asyncio.run(dermo())