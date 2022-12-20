from django.contrib import admin
from .models import Professor, Aluno, Bolsista, Coordenacao, Codesp, SolicitarMatricula, Modalidade, SolicitarModalidade
# Register your models here.
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Bolsista)
admin.site.register(Coordenacao)
admin.site.register(Codesp)
admin.site.register(SolicitarMatricula)
admin.site.register(Modalidade)
admin.site.register(SolicitarModalidade)
