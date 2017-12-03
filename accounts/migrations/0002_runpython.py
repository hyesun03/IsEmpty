from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.hashers import make_password


def forwards_func(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).bulk_create([
        User(username='admin', password=make_password('asdf1234'), email='admin@gmail.com', student_id='00000000', name="관리자", phone_number='01033334444', is_staff=True, is_superuser=True, is_admin=True),
        User(username='chsun0303', password=make_password('asdf1234'), email='chsun0303@gmail.com', name='최혜선', student_id='14109384', phone_number='01011112222', is_admin=True),
        User(username='commonuser01', password=make_password('asdf1234'), email='commonuser01@gmail.com', name='유저1', student_id='14109301', phone_number='01011111234', is_admin=False),
        User(username='commonuser02', password=make_password('asdf1234'), email='commonuser02@gmail.com', name='유저2', student_id='14109302', phone_number='01022221234', is_admin=False),
        User(username='commonuser03', password=make_password('asdf1234'), email='commonuser03@gmail.com', name='유저3', student_id='14109303', phone_number='01033331234', is_admin=False),
    ])


def reverse_func(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).filter(username='admin', email='admin@gmail.com').delete()
    User.objects.using(db_alias).filter(username='chsun0303', email='chsun0303@gmail.com').delete()
    User.objects.using(db_alias).filter(username='commonuser01', email='commonuser01@gmail.com').delete()
    User.objects.using(db_alias).filter(username='commonuser02', email='commonuser02@gmail.com').delete()
    User.objects.using(db_alias).filter(username='commonuser03', email='commonuser03@gmail.com').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
