# Generated by Django 3.2.5 on 2021-07-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibuf', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_admin',
            new_name='UserAdmin',
        ),
        migrations.AlterField(
            model_name='operations',
            name='status',
            field=models.BooleanField(choices=[(True, 'Открыт'), (False, 'Закрыт'), (3, 'Списан')], default=True, verbose_name='Статус'),
        ),
    ]