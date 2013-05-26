# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganizationType'
        db.create_table('site4crm_organizationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('site4crm', ['OrganizationType'])

        # Adding model 'Organization'
        db.create_table('site4crm_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('emaildomain', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.OrganizationType'], null=True)),
        ))
        db.send_create_signal('site4crm', ['Organization'])

        # Adding M2M table for field organization on 'Organization'
        m2m_table_name = db.shorten_name('site4crm_organization_organization')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_organization', models.ForeignKey(orm['site4crm.organization'], null=False)),
            ('to_organization', models.ForeignKey(orm['site4crm.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_organization_id', 'to_organization_id'])

        # Adding model 'Domain'
        db.create_table('site4crm_domain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('site4crm', ['Domain'])

        # Adding model 'Department'
        db.create_table('site4crm_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('site4crm', ['Department'])

        # Adding model 'ContactRole'
        db.create_table('site4crm_contactrole', (
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('site4crm', ['ContactRole'])

        # Adding model 'Contact'
        db.create_table('site4crm_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.Organization'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.ContactRole'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.Department'])),
            ('orgjob', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('site4crm', ['Contact'])

        # Adding M2M table for field contact on 'Contact'
        m2m_table_name = db.shorten_name('site4crm_contact_contact')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_contact', models.ForeignKey(orm['site4crm.contact'], null=False)),
            ('to_contact', models.ForeignKey(orm['site4crm.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_contact_id', 'to_contact_id'])

        # Adding model 'AddressBook'
        db.create_table('site4crm_addressbook', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.Contact'], null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.Organization'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('buildingaddress', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('site4crm', ['AddressBook'])

        # Adding model 'ContactInteractionType'
        db.create_table('site4crm_contactinteractiontype', (
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('site4crm', ['ContactInteractionType'])

        # Adding model 'Interaction'
        db.create_table('site4crm_interaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.Contact'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.ContactInteractionType'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal('site4crm', ['Interaction'])


    def backwards(self, orm):
        # Deleting model 'OrganizationType'
        db.delete_table('site4crm_organizationtype')

        # Deleting model 'Organization'
        db.delete_table('site4crm_organization')

        # Removing M2M table for field organization on 'Organization'
        db.delete_table(db.shorten_name('site4crm_organization_organization'))

        # Deleting model 'Domain'
        db.delete_table('site4crm_domain')

        # Deleting model 'Department'
        db.delete_table('site4crm_department')

        # Deleting model 'ContactRole'
        db.delete_table('site4crm_contactrole')

        # Deleting model 'Contact'
        db.delete_table('site4crm_contact')

        # Removing M2M table for field contact on 'Contact'
        db.delete_table(db.shorten_name('site4crm_contact_contact'))

        # Deleting model 'AddressBook'
        db.delete_table('site4crm_addressbook')

        # Deleting model 'ContactInteractionType'
        db.delete_table('site4crm_contactinteractiontype')

        # Deleting model 'Interaction'
        db.delete_table('site4crm_interaction')


    models = {
        'site4crm.addressbook': {
            'Meta': {'object_name': 'AddressBook'},
            'buildingaddress': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Contact']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Organization']", 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'site4crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'contact_rel_+'", 'null': 'True', 'to': "orm['site4crm.Contact']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Department']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Organization']"}),
            'orgjob': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.ContactRole']"})
        },
        'site4crm.contactinteractiontype': {
            'Meta': {'object_name': 'ContactInteractionType'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'site4crm.contactrole': {
            'Meta': {'object_name': 'ContactRole'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'site4crm.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'site4crm.domain': {
            'Meta': {'object_name': 'Domain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'site4crm.interaction': {
            'Meta': {'object_name': 'Interaction'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Contact']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.ContactInteractionType']"})
        },
        'site4crm.organization': {
            'Meta': {'object_name': 'Organization'},
            'emaildomain': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'organization': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'organization_rel_+'", 'null': 'True', 'to': "orm['site4crm.Organization']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.OrganizationType']", 'null': 'True'})
        },
        'site4crm.organizationtype': {
            'Meta': {'object_name': 'OrganizationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['site4crm']