# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import taggit_autosuggest.managers
import djangocms_text_ckeditor.fields
import app_data.fields
import aldryn_apphooks_config.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cms', '0013_urlconfrevision'),
        ('djangocms_blog', '0007_auto_20150719_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name='type')),
                ('namespace', models.CharField(default=None, unique=True, max_length=100, verbose_name='instance namespace')),
                ('app_data', app_data.fields.AppDataField(default=b'{}', editable=False)),
            ],
            options={
                'verbose_name': 'blog config',
                'verbose_name_plural': 'blog configs',
            },
        ),
        migrations.CreateModel(
            name='BlogConfigTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('app_title', models.CharField(max_length=234, verbose_name='application title')),
                ('object_name', models.CharField(default='Article', max_length=234, verbose_name='object name')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='djangocms_blog.BlogConfig', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'djangocms_blog_blogconfig_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'blog config Translation',
            },
        ),
        migrations.CreateModel(
            name='GenericBlogPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(blank=True, to='djangocms_blog.BlogConfig', help_text='When selecting a value, the form is reloaded to get the updated default', null=True, verbose_name='app. config')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='latestpostsplugin',
            name='tags',
        ),
        migrations.AddField(
            model_name='latestpostsplugin',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='Show only the blog articles tagged with chosen tags.', verbose_name='filter by tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='published since'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published_end',
            field=models.DateTimeField(null=True, verbose_name='published until', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sites',
            field=models.ManyToManyField(help_text='Select sites in which to show the post. If none is set it will be visible in all the configured sites.', to='sites.Site', verbose_name='Site(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='abstract',
            field=djangocms_text_ckeditor.fields.HTMLField(default='', verbose_name='abstract', blank=True),
        ),
        migrations.AddField(
            model_name='authorentriesplugin',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(blank=True, to='djangocms_blog.BlogConfig', help_text='When selecting a value, the form is reloaded to get the updated default', null=True, verbose_name='app. config'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(verbose_name='app. config', to='djangocms_blog.BlogConfig', help_text='When selecting a value, the form is reloaded to get the updated default', null=True),
        ),
        migrations.AddField(
            model_name='latestpostsplugin',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(blank=True, to='djangocms_blog.BlogConfig', help_text='When selecting a value, the form is reloaded to get the updated default', null=True, verbose_name='app. config'),
        ),
        migrations.AddField(
            model_name='post',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(verbose_name='app. config', to='djangocms_blog.BlogConfig', help_text='When selecting a value, the form is reloaded to get the updated default', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='blogconfigtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
