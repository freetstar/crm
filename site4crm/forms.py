#!/usr/bin/env python2
#-*- coding=utf-8 -*-

from django.forms import ModelForm ,Select
from models import StateCityArea

class StateCityAreaForm(ModelForm):
      class Meta:
          model   = StateCityArea
          fields  = ('state','city','area')
          widgets = {'state':Select(),'city':Select(),'area':Select()}
