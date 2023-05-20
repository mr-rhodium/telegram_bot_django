from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.user import USER_TELEGRAM
from django.conf import settings

router = Router()


@router.message(Command(commands=["start"]))

async def heandle_start_command(message: Message) -> None:
    if message.from_user is None:
        return 
    
    _, is_new = await USER_TELEGRAM.registrer_bot_user(

        user_is=message.from_user.id,
        chat_id=message.chat.id,
        username=message.from_user.username
    )
    if is_new:
        await message.answer("New User")
    else:
        await message.answer("Old user")

@router.message(Command(commands=["apps"]))
async def heand_apps(message: Message):
    apps_name = [app_name for app_name in settings.INSTALLED_APPS]
    await message.answer(f"apps: {apps_name}")


@router.message(Command(commands=["id"]))
async def handle_id_command(message: Message) -> None:
    if message.from_user is None:
        return
    
    await message.answer(
        f"User Id"
    )