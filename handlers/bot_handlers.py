from aiogram import F, Router
from aiogram.types import Message
import subprocess

router = Router()


@router.message(F.text)
async def add_download(message: Message):
    if "magnet:" in message.text:
        output = subprocess.run(['transmission-remote', '-a', f'{message.text}'], capture_output=True, text=True)
        text = output.stdout
        if 'responded: "success"' in text:
            await message.answer("Download Your file")
        else:
            await message.answer(text)
    else:
        await message.answer("Не магнет-ссылка")
