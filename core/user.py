from typing import Final

from core.models import TUser

class CodeUser:
    @staticmethod
    async def registrer_bot_user(
        user_id: int,
        chat_id:int,
        username: str ) -> tuple[TUser, bool]:
        return await TUser.objects.aget_or_create(
        id=user_id,
        chat_id=chat_id,
        username=username
    )

USER_TELEGRAM: Final[CodeUser] = CodeUser()