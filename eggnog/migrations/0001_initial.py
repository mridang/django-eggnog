# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Update'
        db.create_table('eggnog_update', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2000)),
            ('installed', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('available', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('checked', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('eggnog', ['Update'])


    def backwards(self, orm):
        # Deleting model 'Update'
        db.delete_table('eggnog_update')


    models = {
        'eggnog.update': {
            'Meta': {'ordering': "['-checked']", 'object_name': 'Update'},
            'available': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'checked': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'package': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2000'})
        }
    }

    complete_apps = ['eggnog']
