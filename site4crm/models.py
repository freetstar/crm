#coding:utf-8
from django.db import models

# Create your models here.

class OrganizationType(models.Model):
    key  = models.CharField('key',max_length = 30,unique = True)
    name = models.CharField(max_length       = 30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = ('组织类型')

class Organization(models.Model):
    name         = models.CharField(max_length                = 15)
    emaildomain  = models.CharField(max_length                = 20)
    organization = models.ManyToManyField('self',blank        = True,null = True)
    type         = models.ForeignKey(OrganizationType,null = True)

    def _address(self):
        """return the address or None"""
        try:
            return self.adressbook_set.get()
        except AddressBook.DoesNotExist:
            return None
    address = property(_address)    

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = ("组织")

class Domain(models.Model):
    """客户领域"""
    key     = models.CharField(max_length=5)
    name    = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name ="客户领域"

class Department(models.Model):
    """部门"""
    key     = models.CharField(max_length=5)
    name    = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name ="部门"

class ContactRole(models.Model):
    key  = models.CharField(max_length = 20,unique = True,primary_key = True)
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name  = "联系人角色"

class Contact(models.Model):
    ORGANIZATION_RULE = (
        ('1','Role1'),
        ('2','Role2'),
    )
    name         = models.CharField(max_length         = 30)
    phone1       = models.CharField(max_length         = 20)
    phone2       = models.CharField(max_length         = 20)
    email        = models.EmailField(blank             = True,max_length = 75)
    organization = models.ForeignKey(Organization)
    role         = models.ForeignKey(ContactRole)
    department   = models.ForeignKey(Department)
    orgjob       = models.CharField(max_length         = 20,blank        = True)
    contact      = models.ManyToManyField('self',blank = True,null       = True)

    def _address(self):
        """return the address or None"""
        try:
            return self.adressbook_set.get()
        except AddressBook.DoesNotExist:
            return None
    address = property(_address)    

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name   =  "联系人"

class AddressBook(models.Model):  
    """
    Address information associated with a contact and an organization
    """
    contact         = models.ForeignKey(Contact,blank=True,null=True)
    organization    = models.ForeignKey(Organization,blank=True,null=True)
    description     = models.CharField( max_length    = 20, blank = True)
    province        = models.CharField( max_length    = 5)
    city            = models.CharField( max_length    = 5)
    country         = models.CharField( max_length    = 5, blank  = True)
    street          = models.CharField( max_length    = 80)
    buildingaddress = models.CharField( max_length    = 10)
    postal_code     = models.CharField( max_length    = 6)

    def __unicode__(self):
       return u'%s - %s' % (self.contact.name, self.description)


    class Meta:
        verbose_name   =   "地址簿"

class ContactInteractionType(models.Model):
    key = models.CharField(max_length=30, unique=True, primary_key=True)
    name = models.CharField(max_length=40)

class Interaction(models.Model):
    """
    A type of activity with the customer.  Useful to track emails, phone calls,
    or in-person interactions.
    """
    contact = models.ForeignKey(Contact)
    type = models.ForeignKey(ContactInteractionType)
    date_time = models.DateTimeField()
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.contact.name, self.type)

    class Meta:
        verbose_name = "客户交互"
