# Generated by Django 4.1.7 on 2023-04-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_pic', verbose_name='Аватар'),
        ),
    ]
