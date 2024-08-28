# Generated by Django 4.2.15 on 2024-08-28 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Waiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.domain')),
                ('error_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.errorcode')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waivers.module')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.project')),
            ],
        ),
        migrations.CreateModel(
            name='WaiverType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WaiverApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.approver')),
                ('waiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.waiver')),
            ],
        ),
        migrations.AddField(
            model_name='waiver',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.waivertype'),
        ),
        migrations.AddField(
            model_name='domain',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waivers.project'),
        ),
        migrations.AddField(
            model_name='approver',
            name='domain',
            field=models.ManyToManyField(to='waivers.domain'),
        ),
        migrations.AddField(
            model_name='approver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='approver',
            name='waiver_type',
            field=models.ManyToManyField(to='waivers.waivertype'),
        ),
    ]
