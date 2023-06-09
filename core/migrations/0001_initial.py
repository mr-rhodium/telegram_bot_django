# Generated by Django 4.2.1 on 2023-05-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Telegram Id Number')),
                ('chat_id', models.BigIntegerField(verbose_name='Telegram Chat ID')),
                ('username', models.CharField(max_length=64, verbose_name='Telegram Username')),
            ],
            options={
                'db_table': 'telegram_user',
            },
        ),
    ]
