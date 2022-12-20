from django.shortcuts import render, redirect
from django.views import View


from .models import Modalidade, SolicitarModalidade, SolicitarMatricula, Bolsista, Aluno
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/index.html')

class BolsistaView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'criarModalidade': Modalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all(),
        'Bolsista':Bolsista.objects.all(), 'Aluno':Aluno.objects.all()}
        return render(request, 'codesp/bolsista/index.html', contexto)

    def post(self, request, *args, **kwargs):
        aluno_id = request.POST.get('aluno_id')
        modalidade = request.POST.get('modalidade_id')
        categoria = request.POST.get('categoria')
        bolsista = request.POST.get('bolsista_id')
        if aluno_id and modalidade and categoria and bolsista:
            novo = SolicitarMatricula(tipoCategoria=categoria, modalidade_id=modalidade, bolsista_id = bolsista, aluno_id=aluno_id)
            novo.save()
            return redirect('/autorizarMatricula', {'SolicitarMatricula' : SolicitarMatricula.objects.all()})

        else:
            return redirect('/espacoModalidade',{'Bolsista':Bolsista.objects.all(),'criarModalidade': Modalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all()})

class CodespView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'SolicitarMatricula' : SolicitarMatricula.objects.all()}
        return render(request, 'codesp/codesp/index.html', contexto)


class ProfessorView(View):
    contexto = {'criarModalidade': Modalidade.objects.all()}
    def get(self, request, *args, **kwargs):

        return render(request, 'codesp/professor/index.html', self.contexto)

    def post(self, request, *args, **kwargs):
        horarioInicial = request.POST.get('horarioInicial')
        horarioFinal = request.POST.get('horarioFinal')
        justificativa = request.POST.get('justificativa')
        modalidade = request.POST.get('modalidade_id')
        categoria = request.POST.get('categoria')
        if horarioInicial and horarioFinal and justificativa and categoria and modalidade:
            novo = SolicitarModalidade(horarioInicial=horarioInicial, horarioFinal=horarioFinal, justificativa=justificativa,professor_id=1, modalidade_id=modalidade, categoria=categoria)
            novo.save()
            return redirect('/espacoModalidade', {'criarModalidade': Modalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all(),
        'Bolsista':Bolsista.objects.all(), 'Aluno':Aluno.objects.all()})

        else:
            return redirect('/solicitacao',{ 'criarModalidade': Modalidade.objects.all()})




class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/professor/frequencia.html')

