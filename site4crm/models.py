#coding:utf-8
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

class ContactOrganization(models.Model):
    key  = models.CharField('key',max_length = 30,unique = True)
    name = models.CharField(max_length       = 30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = ('组织类型')

class Organization(models.Model):
    name         = models.CharField(max_length             = 15)
    emaildomain  = models.CharField(max_length             = 20)
    organization = models.ManyToManyField('self',blank     = True,null = True)
    orgtype      = models.ForeignKey(ContactOrganization,null = True)

    def _address(self):
        """return the address or None"""
        try:
            return self.adressbook_set.get(organization=self)
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
    """标准部门"""
    key     = models.CharField(max_length=5)
    name    = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name ="标准部门"

class ContactRole(models.Model):
    key  = models.CharField(max_length = 20,unique = True,primary_key = True)
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name  = "联系人角色"

class Contact(models.Model):
    """
    A customer, supplier or any individual that a store owner might interact
    with.
    """
    title  = models.CharField(_("Title"), max_length = 30, blank = True, null = True)
    name   = models.CharField(_("Name"), max_length  = 30, )
    #Todo add 名字缩写模型
    phone1 = models.CharField(max_length             = 20)
    phone2 = models.CharField(max_length             = 20)
    email = models.EmailField(_("Email"), blank=True, max_length=75)

    def _address(self):
        """return the address or None"""
        try:
            return self.adressbook_set.get(contact=self)
        except AddressBook.DoesNotExist:
            return None
    address = property(_address)    
    department   = models.ForeignKey(Department)
    organization = models.ForeignKey(Organization, verbose_name = _("Organization"), blank = True)
    role         = models.ForeignKey('ContactRole', verbose_name  = _("Role"), )
    orgjob       = models.CharField(max_length                  = 20,blank                 = True)
    domain       = models.ForeignKey(Domain,null=True) 
    contact      = models.ManyToManyField('self',blank = True,null       = True)
    #user = models.ForeignKey(User, blank=True, null=True, unique=True)

    def _get_address_book_entries(self):
        """ Return all non primary shipping and billing addresses
        """
        return AddressBook.objects.filter(contact=self.pk).exclude(is_default_shipping=True).exclude(is_default_billing=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

class StateCityArea(models.Model):
    state           = models.CharField( max_length    = 5)
    city            = models.CharField( max_length    = 5)
    area            = models.CharField( max_length    = 5)

class AddressBook(models.Model):  
    """
    Address information associated with a contact and an organization
    """
    contact         = models.ForeignKey(Contact,blank=True,null=True)
    organization    = models.ForeignKey(Organization,blank=True,null=True)
    description     = models.CharField( max_length    = 20, blank = True)
    statecityarea   = models.ForeignKey(StateCityArea,blank=True )
    street          = models.CharField( max_length    = 80)
    buildingaddress = models.CharField( max_length    = 10)
    postal_code     = models.CharField( max_length    = 6)

    def __unicode__(self):
       return u'%s - %s' % (self.contact.name, self.description)

    class Meta:
        verbose_name  =  "地址簿"

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
