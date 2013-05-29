#!/usr/bin/env python2
#-*- coding=utf-8 -*-
from models import Organization,ContactOrganization,Domain,Department,Contact,ContactRole,StateCityArea,AddressBook,ContactInteractionType,Interaction,StateCityArea
from django.contrib import admin



class AddressBookInline(admin.StackedInline):
    model = AddressBook
    extra = 1

class ContactAdmin(admin.ModelAdmin):
    inlines = [AddressBookInline]

admin.site.register(Contact,ContactAdmin)


admin.site.register(Organization)
admin.site.register(ContactOrganization)
admin.site.register(Domain)
admin.site.register(Department)
admin.site.register(StateCityArea)
admin.site.register(AddressBook)
admin.site.register(ContactRole)
admin.site.register(ContactInteractionType)
admin.site.register(Interaction)
