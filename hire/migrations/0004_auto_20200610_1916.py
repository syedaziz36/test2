# Generated by Django 2.2 on 2020-06-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0003_auto_20200610_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile1',
            old_name='message_toC',
            new_name='tag_line',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='company_link',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='skills',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='techgig_points',
            field=models.CharField(blank=True, default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='company_logo',
            field=models.FileField(upload_to='hire/images'),
        ),
        migrations.AlterField(
            model_name='userprofile1',
            name='codechef_points',
            field=models.CharField(blank=True, default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile1',
            name='codeforces_points',
            field=models.CharField(blank=True, default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile1',
            name='profile_pic',
            field=models.FileField(upload_to='hire/images'),
        ),
        migrations.AlterField(
            model_name='userprofile1',
            name='stackoverflow_points',
            field=models.CharField(blank=True, default=' ', max_length=200),
        ),
    ]
