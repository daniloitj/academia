from django.db import models

# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.localflavor.br.br_states import STATE_CHOICES
GENERO = (('M','masculino'),('F','feminino'))
ESTADOCIVEL = (('Solteiro','solteiro'),('Casado','casado'))

class Pessoa(models.Model):
    """ Classe que representa todas pessoas envolvidas no sistema,
	ou seja; clientes, funcionario, representantes, fornecedores,...
	Apresenta como chave o id, nome e email.
    """
    class Meta:
        abstract = True
        db_table = "Pessoa"
        ordering = ('nome',)
        unique_together = (('nome', 'email'),)			
    nome = models.CharField(max_length=400)
    telefone = models.CharField(max_length=400, blank=True, null=True)
    site = models.CharField(max_length=400, blank=True, null=True)
    celular = models.CharField(max_length=400, blank=True, null=True)
    fax = models.CharField(max_length=400, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    endereco =  models.CharField(max_length=300, blank=True)
    descricao =  models.TextField(blank=True, null=True)
    numero_da_casa = models.CharField(max_length=100, blank=True, null=True)
    data_de_cadastro = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="data de cadastro no Sistema", auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="data de castro no Sistema", auto_now_add=True)
    def __unicode__(self):
        return self.nome 

    def get_absolute_url(self):
        return 'pessoa/%d/'%self.id

class PessoaFisica(Pessoa):
    """ Classe abstrata, que herda caracateristicas da Classe Pessoa,
	fornece uma especificacao para Pessoas Fisicas envolvidas com o sistema.
    """
    class Meta:
        abstract = True
        unique_together = (('pessoa', 'cpf','rg'),)			
    sobrenome = models.CharField(max_length=100)
    genero = models.CharField(max_length=20,choices=GENERO,blank=True)
    cpf = models.CharField(max_length=100, unique=True)
    rg = models.CharField(max_length=100, unique=True)
    data_de_nascimento = models.DateTimeField(default=datetime.now, blank=True, null=True,verbose_name="data de Nascimento")
    def get_nome_mais_sobrenome(self):
        return self.pessoa.nome + ' ' + self.sobrenome


class Aluno(PessoaFisica):
    """ Classe responssavel pela definicao de Aluno.
	Filha da Classe PessoaFisica
    """
    class Meta:
        verbose_name = u'Aluno' 
        verbose_name_plural = u'Aluno' 
        db_table = 'Aluno'		
    def __unicode__(self):
         return self.pessoa.nome + ' ' + self.sobrenome + '  -------- CPF:  ' + self.cpf

    def get_absolute_url(self):
        return '%d/'%self.id

		




	