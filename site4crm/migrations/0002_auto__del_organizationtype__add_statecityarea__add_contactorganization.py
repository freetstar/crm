# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'OrganizationType'
        db.delete_table('site4crm_organizationtype')

        # Adding model 'StateCityArea'
        db.create_table('site4crm_statecityarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('site4crm', ['StateCityArea'])

        # Adding model 'ContactOrganization'
        db.create_table('site4crm_contactorganization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('site4crm', ['ContactOrganization'])

        # Adding field 'Contact.title'
        db.add_column('site4crm_contact', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.domain'
        db.add_column('site4crm_contact', 'domain',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.Domain'], null=True),
                      keep_default=False)

        # Deleting field 'Organization.type'
        db.delete_column('site4crm_organization', 'type_id')

        # Adding field 'Organization.orgtype'
        db.add_column('site4crm_organization', 'orgtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.ContactOrganization'], null=True),
                      keep_default=False)

        # Deleting field 'AddressBook.province'
        db.delete_column('site4crm_addressbook', 'province')

        # Deleting field 'AddressBook.city'
        db.delete_column('site4crm_addressbook', 'city')

        # Deleting field 'AddressBook.country'
        db.delete_column('site4crm_addressbook', 'country')

        # Adding field 'AddressBook.statecityarea'
        db.add_column('site4crm_addressbook', 'statecityarea',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['site4crm.StateCityArea'], blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'OrganizationType'
        db.create_table('site4crm_organizationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('site4crm', ['OrganizationType'])

        # Deleting model 'StateCityArea'
        db.delete_table('site4crm_statecityarea')

        # Deleting model 'ContactOrganization'
        db.delete_table('site4crm_contactorganization')

        # Deleting field 'Contact.title'
        db.delete_column('site4crm_contact', 'title')

        # Deleting field 'Contact.domain'
        db.delete_column('site4crm_contact', 'domain_id')

        # Adding field 'Organization.type'
        db.add_column('site4crm_organization', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site4crm.OrganizationType'], null=True),
                      keep_default=False)

        # Deleting field 'Organization.orgtype'
        db.delete_column('site4crm_organization', 'orgtype_id')


        # User chose to not deal with backwards NULL issues for 'AddressBook.province'
        raise RuntimeError("Cannot reverse this migration. 'AddressBook.province' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AddressBook.city'
        raise RuntimeError("Cannot reverse this migration. 'AddressBook.city' and its values cannot be restored.")
        # Adding field 'AddressBook.country'
        db.add_column('site4crm_addressbook', 'country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)

        # Deleting field 'AddressBook.statecityarea'
        db.delete_column('site4crm_addressbook', 'statecityarea_id')


    models = {
        'site4crm.addressbook': {
            'Meta': {'object_name': 'AddressBook'},
            'buildingaddress': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Contact']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Organization']", 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'statecityarea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.StateCityArea']", 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'site4crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'contact_rel_+'", 'null': 'True', 'to': "orm['site4crm.Contact']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Department']"}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Domain']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.Organization']", 'blank': 'True'}),
            'orgjob': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.ContactRole']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'site4crm.contactinteractiontype': {
            'Meta': {'object_name': 'ContactInteractionType'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'site4crm.contactorganization': {
            'Meta': {'object_name': 'ContactOrganization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'orgtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site4crm.ContactOrganization']", 'null': 'True'})
        },
        'site4crm.statecityarea': {
            'Meta': {'object_name': 'StateCityArea'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['site4crm']