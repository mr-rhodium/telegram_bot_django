from django.db import models

class TUser(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name="Telegram Id Number")

    chat_id = models.BigIntegerField(verbose_name="Telegram Chat ID")

    username = models.CharField(max_length=64, verbose_name="Telegram Username")

    objects: models.manager.BaseManager["TUser"]

    class Meta:
        db_table = "telegram_user"
        verbose_name = "Telegram user"
        verbose_name_plural = "Telegram users"