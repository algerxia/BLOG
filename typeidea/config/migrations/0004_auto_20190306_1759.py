# Generated by Django 2.1.7 on 2019-03-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20190306_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '展示'), (0, '隐藏')], default=1, verbose_name='状态'),
        ),
    ]
