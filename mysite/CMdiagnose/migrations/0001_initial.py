# Generated by Django 2.2.1 on 2019-05-21 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gum', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('heart', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('head', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('liver', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('spleen', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('stomach', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('kidney', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('lips', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('face', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('nose', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('throat', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('pulse', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('general', models.CharField(blank=True, default='normal', max_length=2000, null=True)),
                ('temperment', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('result', models.CharField(blank=True, default='normal', max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facts', models.CharField(blank=True, default='nothing', max_length=200, null=True)),
                ('symptom', models.CharField(blank=True, default='nothing', max_length=200, null=True)),
                ('solution', models.CharField(blank=True, default='nothing', max_length=200, null=True)),
                ('reference', models.CharField(blank=True, default='nothing', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tongue',
            fields=[
                ('body', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CMdiagnose.Body')),
                ('tip', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('root', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('side', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('middle', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('fur', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('fluid', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('color', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('moisture', models.CharField(blank=True, default='normal', max_length=200, null=True)),
                ('bottom', models.CharField(blank=True, default='normal', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CMdiagnose.Body')),
                ('tongue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CMdiagnose.Tongue')),
            ],
        ),
    ]
