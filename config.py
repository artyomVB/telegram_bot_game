from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Объект бота
bot = Bot(token="")  # Сюда вставить токен

# Диспетчер для бота
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
