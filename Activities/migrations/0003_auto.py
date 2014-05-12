# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field attendees on 'OnthemoveActivity'
        m2m_table_name = db.shorten_name(u'Activities_onthemoveactivity_attendees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('onthemoveactivity', models.ForeignKey(orm[u'Activities.onthemoveactivity'], null=False)),
            ('onthemoveuser', models.ForeignKey(orm[u'Users.onthemoveuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['onthemoveactivity_id', 'onthemoveuser_id'])


    def backwards(self, orm):
        # Removing M2M table for field attendees on 'OnthemoveActivity'
        db.delete_table(db.shorten_name(u'Activities_onthemoveactivity_attendees'))


    models = {
        u'Activities.onthemoveactivity': {
            'Meta': {'object_name': 'OnthemoveActivity'},
            'activity_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'activity_img': ('django.db.models.fields.files.ImageField', [], {'default': "'static/Activities/img/activity/default_act.jpg'", 'max_length': '100'}),
            'activity_name': ('django.db.models.fields.TextField', [], {'max_length': '40'}),
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'a+'", 'symmetrical': 'False', 'to': u"orm['Users.OnthemoveUser']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Activities.OnthemoveLocation']"}),
            'max_num_attendees': ('django.db.models.fields.IntegerField', [], {}),
            'min_num_attendees': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'owner_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'o+'", 'to': u"orm['Users.OnthemoveUser']"}),
            'skill_level': ('django.db.models.fields.TextField', [], {'default': "'Beginner'", 'max_length': '2'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'Activities.onthemovelocation': {
            'Meta': {'object_name': 'OnthemoveLocation'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_img': ('django.db.models.fields.files.ImageField', [], {'default': "'static/Activities/img/locations/default_loc.jpg'", 'max_length': '100'}),
            'location_name': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'location_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'Users.onthemoveuser': {
            'Meta': {'object_name': 'OnthemoveUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'default': "'static/Users/img/user_img/default_user.jpg'", 'max_length': '100', 'null': 'True'}),
            'phoneNumber': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '10'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Activities']