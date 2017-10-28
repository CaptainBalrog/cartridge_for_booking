# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-16 13:41
from __future__ import unicode_literals

import cartridge.shop.fields
from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_content_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content_de',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='category',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='category',
            name='content_es',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='category',
            name='content_fr',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='category',
            name='content_nl',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title_de',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title_en',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title_es',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title_fr',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title_nl',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_de',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_es',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_fr',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_nl',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_es',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_nl',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_de',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_es',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_fr',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_nl',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='description_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='description_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='description_es',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='description_fr',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='description_nl',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='name_de',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='name_en',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='name_es',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='name_fr',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productoption',
            name='name_nl',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option1_de',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option1_en',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option1_es',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option1_fr',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option1_nl',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option2_de',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option2_en',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option2_es',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option2_fr',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='option2_nl',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour'),
        ),
    ]