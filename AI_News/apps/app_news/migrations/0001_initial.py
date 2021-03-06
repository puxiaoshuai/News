# Generated by Django 2.1.5 on 2019-01-18 09:21

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'userprofile',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('img_url', models.CharField(max_length=200)),
                ('img_tv_url', models.CharField(max_length=120)),
                ('tv_name', models.CharField(max_length=120)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'news',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '新闻分类',
                'verbose_name_plural': '新闻分类',
                'db_table': 'news_tag',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='newstag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='news', to='app_news.NewsTag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment', to='app_news.News'),
        ),
    ]
