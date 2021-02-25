# Generated by Django 3.1.1 on 2021-02-25 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(verbose_name='Exam Date')),
                ('exam_name', models.CharField(max_length=200)),
                ('total_marks', models.FloatField(default=0)),
                ('pass_marks', models.FloatField(default=0)),
                ('exam_status', models.BooleanField(default=False)),
            ],
        ),
    ]
