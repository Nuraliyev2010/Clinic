# Generated by Django 4.2.4 on 2023-10-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_employee_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='section',
            field=models.CharField(default=1, max_length=25, verbose_name='Bo`limi :'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ish haqi :'),
        ),
    ]
