# Generated by Django 4.1.7 on 2023-02-15 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('class_section', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('member_type', models.TextField(choices=[('STUDENT', 'Student'), ('TA', 'Teacher Assistant'), ('INSTRUCTOR', 'Instructor')])),
                ('classes', models.ManyToManyField(to='qanow.class')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('prompt', models.CharField(max_length=256)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.TextField(choices=[('SYLLABUS', 'Syllabus'), ('EXAM', 'Exam'), ('HW', 'Homework'), ('MISC', 'Misc')])),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qanow.member')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('prompt', models.CharField(max_length=256)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='qanow.member')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='qanow.question')),
            ],
        ),
    ]