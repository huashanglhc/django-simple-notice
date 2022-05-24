# Generated by Django 4.0.4 on 2022-05-23 11:39
import django

if django.VERSION > (4, 0):
    from django.db.models import JSONField
else:
    from django.contrib.postgres.fields import JSONField
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_alter_receivertag_noticestore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='latest update time')),
                ('receiver', models.CharField(max_length=64, verbose_name='receiver')),
                ('is_read', models.BooleanField(default=False, verbose_name='read status')),
                ('read_at', models.DateTimeField(null=True, verbose_name='read time')),
                ('data', JSONField(null=True, verbose_name='data')),
                ('is_done', models.BooleanField(default=False, verbose_name='completed status')),
                ('done_at', models.DateTimeField(null=True, verbose_name='completed datetime')),
                ('handler', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None, verbose_name='handler')),
                ('initiator', models.CharField(max_length=64, null=True, verbose_name='initiator')),
                ('initiator_name', models.CharField(max_length=64, null=True, verbose_name='initiator name')),
                ('obj_name', models.CharField(max_length=64, null=True, verbose_name='obj name')),
                ('obj_key', models.CharField(max_length=64, null=True, verbose_name='obj key')),
                ('obj_status', models.CharField(max_length=64, null=True, verbose_name='obj status')),
                ('batch', models.CharField(max_length=36, null=True, verbose_name='batch')),
                ('candidates', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), null=True, size=None, verbose_name='candidates')),
            ],
            options={
                'db_table': 'notice_backlog',
            },
        ),
        migrations.CreateModel(
            name='PrivateNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='latest update time')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='creator')),
                ('receiver', models.CharField(max_length=64, verbose_name='receiver')),
                ('content', models.TextField(null=True, verbose_name='content')),
                ('title', models.CharField(max_length=64, null=True, verbose_name='title')),
                ('is_read', models.BooleanField(default=False, verbose_name='read status')),
                ('read_at', models.DateTimeField(null=True, verbose_name='read time')),
            ],
            options={
                'db_table': 'notice_private_notice',
            },
        ),
    ]
