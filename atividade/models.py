from django.db import models

# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from rh.models import Professor, Aluno

class Atividade(models.Model):
    """ descricao de atividade fisica
    """
    class Meta:
        db_table = "Atividade"			
    nome = models.CharField(max_length=400)
    descricao =  models.TextField(blank=True, null=True)
    data_de_cadastro = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="data de cadastro no Sistema", auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="data de castro no Sistema", auto_now_add=True)
    def __unicode__(self):
        return self.nome 

    def get_absolute_url(self):
        return 'aitividade/%d/'%self.id 

class AtividadeAluno(models.Model):
    """ uniao entre atividade aluno e professor
    """		
    professor = models.ForeignKey(Professor, unique=True)
    aluno = models.ForeignKey(Aluno, unique=True)
    atividade = models.ForeignKey('Atividade', unique=True)
    serie = models.PositiveIntegerField(default=1, verbose_name="quantidade de series")
    repeticoes = models.PositiveIntegerField(default=1, verbose_name="quantidade de repeticoes")
    data_de_cadastro = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="data de cadastro no Sistema", auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="data de castro no Sistema", auto_now_add=True)
    def __unicode__(self):
        return self.nome 

    def get_absolute_url(self):
        return 'aitividadealuno/%d/'%self.id 
