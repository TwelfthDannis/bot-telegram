
from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer("I've sent your message to myself.")
    except TypeError:
        await message.answer("Nice try!")