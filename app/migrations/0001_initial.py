# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idea'
        db.create_table(u'app_idea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'app', ['Idea'])


    def backwards(self, orm):
        # Deleting model 'Idea'
        db.delete_table(u'app_idea')


    models = {
        u'app.idea': {
            'Meta': {'object_name': 'Idea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['app']