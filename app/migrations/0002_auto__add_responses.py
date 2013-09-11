# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Responses'
        db.create_table(u'app_responses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Responses'])


    def backwards(self, orm):
        # Deleting model 'Responses'
        db.delete_table(u'app_responses')


    models = {
        u'app.idea': {
            'Meta': {'object_name': 'Idea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'app.responses': {
            'Meta': {'object_name': 'Responses'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']