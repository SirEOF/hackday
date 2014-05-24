# -*- coding: utf-8 -*-

from django import forms
from  DjangoUeditor.forms import UEditorField


class TestUEditorForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = UEditorField(u"描述", initial="", width=1100, height=400)
