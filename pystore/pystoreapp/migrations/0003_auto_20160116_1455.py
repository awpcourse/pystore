# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pystoreapp', '0002_auto_20160116_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(to='pystoreapp.Product'),
        ),
    ]
