from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
import os

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Пришли мне магнет-ссылку:")


@router.message(F.text)
async def character_name(message: Message):
    if "magnet:" in message.text:
        command = f'transmission-remote -a "{message.text}"'
        os.system(command)
    else:
        await message.answer("Не магнет-ссылка")
