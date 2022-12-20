from django.db import models

# Create your models here.



class Professor(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome}'

class Bolsista(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.turno}'

class Aluno(models.Model):
    nomeAluno = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nomeAluno} - {self.matricula}'

class Coordenacao(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nome} - {self.matricula}'


class Modalidade(models.Model):
    nomeModalidade = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nomeModalidade}'



class SolicitarModalidade(models.Model):
    dataPedido = models.DateTimeField(auto_now_add=True, blank=True)
    categoria = models.CharField(max_length=20)
    horarioInicial = models.CharField(max_length=10)
    horarioFinal = models.CharField(max_length=10)
    justificativa = models.CharField(max_length = 80)
    modalidade = models.ForeignKey(Modalidade, on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.professor} - {self.modalidade} - {self.categoria}'


class SolicitarMatricula(models.Model):
    tipoCategoria = models.CharField(max_length=40)
    dataInscricao = models.DateTimeField(auto_now_add=True, blank=True)
    aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    modalidade = models.ForeignKey(SolicitarModalidade, on_delete = models.CASCADE)
    bolsista = models.ForeignKey(Bolsista, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.aluno} - {self.modalidade} - {self.tipoCategoria}'


class Codesp(models.Model):
    solicitacao = models.ForeignKey(SolicitarMatricula, on_delete = models.CASCADE)
    coordenacao = models.ForeignKey(Coordenacao, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.solicitacao} - {self.coordenacao}'


