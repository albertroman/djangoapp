# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postear',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(null=True, blank=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
