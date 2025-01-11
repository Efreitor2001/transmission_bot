from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import subprocess
from aiogram.enums import ParseMode

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Пришли мне магнет-ссылку:")


@router.message(Command("status"))
async def status(message: Message):
    output = subprocess.run(['transmission-remote', '-l'], capture_output=True, text=True)
    text = output.stdout
    await message.answer(f"```Download_Status\n{text}\n```", parse_mode=ParseMode.MARKDOWN_V2)
