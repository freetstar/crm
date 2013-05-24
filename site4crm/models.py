#coding:utf-8
from django.db import models

# Create your models here.

class ContactOrganization(models.Model):
    key          =  models.CharField('key',max_length=30,unique=True)
    name         =  models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = ('contanct organization type')

class Organization(models.Model):
    name         =  models.CharField(max_length=15)
    emaildomain  =  models.CharField(max_length=20)
    organization =  models.ManyToManyField('self',blank=True,null=True)
    type         =  models.ForeignKey(ContactOrganization,null=True)

    class Meta:
        verbose_name = ("组织")

class Contact(models.Model):
    ORGANIZATION_RULE = (
        ('1','Role1'),
        ('2','Role2'),
    )
    name         =   models.CharField(max_length=30)
    phone1       =   models.CharField(max_length=20)
    phone2       =   models.CharField(max_length=20)
    email        =   models.EmailField(blank=True,max_length=75)
    organization =   models.ForeignKey(Organization)
    job          =   models.CharField(max_length=20,blank=True)
    contact      =   models.ManyToManyField('self',blank=True,null=True)

    def _address(self):
        """return the address or None"""
        try:
            return self.adressbook_set.get()
        except AddressBook.DoesNotExist:
            return None
    address = property(_address)    

    def _department(self):
        """try the department it belong"""
        try:
            return self.department_set.get()
        except Department.DoesNotExist:
            return None
    department = property(_department)    


class Domain(models.Model):
    """客户领域"""
    name    =   models.CharField(max_length=15)
    contact =   models.ForeignKey(Contact)

class Department(models.Model):
    """部门"""
    key     = models.CharField(max_length=5)
    name    = models.CharField(max_length=15)

class AddressBook(models.Model):  
    """
    Address information associated with a contact
    """
    contact = models.ForeignKey(Contact)
    organization = models.ForeignKey(Organization)
    description = models.CharField(max_length=20, blank=True)
    addressee = models.CharField( max_length=80)
    street1 = models.CharField( max_length=80)
    street2 = models.CharField(max_length=80, blank=True)
    state = models.CharField( max_length=50, blank=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField( max_length=30)

    def __unicode__(self):
       return u'%s - %s' % (self.contact.name, self.description)
