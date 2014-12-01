# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website_name', models.CharField(max_length=200)),
                ('website_url', models.CharField(max_length=3000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
