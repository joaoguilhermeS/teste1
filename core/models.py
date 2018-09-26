from django.db import models

class Aluno(models.Model):
    dt = models.DateTimeField()
    nome = models.CharField(max_length=40)
    matrícula = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=10)
    observações = models.TextField(null=True, blank=True)
   
    def __stf__(self):
          return self.nome


class Notificacao(models.Model): 
     dt = models.DateTimeField()
     notificacão = models.TextField(null=False, blank=False)
     class Meta:
        verbose_name_plural = 'Notificações'
     pass

class SelecionarPresencaseFaltas(models.Model):
     aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
     class Meta:
        verbose_name_plural = 'SelecionarPresenças e Faltas'
     pass

class Cargo(models.Model):
     cargo = models.CharField(max_length=20)
     funçao = models.CharField(max_length=50)     
     class Meta:
        verbose_name_plural = 'Cargos'
     pass


class Servidor(models.Model):
    dt = models.DateTimeField()
    nome = models.CharField(max_length=40)
    matricula = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=10)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Servidores'
        ordering = ['nome']
    
    def __stf__(self):
          return self.nome
    pass

class Notificacao(models.Model): 
     dt = models.DateTimeField()
     notificacão = models.TextField(null=False, blank=False)
     servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
     class Meta:
        verbose_name_plural = 'Notificações'
     pass

class Adicionar_Justificativa_de_Falta(models.Model): 
     dt = models.DateTimeField()
     Descrição = models.TextField(null=False, blank=False)
     aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
     class Meta:
        verbose_name_plural = 'Adicionar Justificativas de Faltas'
     pass

class GerarDeclaracaoEstudantil(models.Model):
     dt = models.DateTimeField()
     matrícula = models.DecimalField(max_digits=10, decimal_places=0)
     class Meta:
        verbose_name_plural = 'Gerar Declarações Estudantis'
     pass

class GerarListasDePresenca(models.Model):
     dt = models.DateTimeField()
     alunos = models.ForeignKey(Aluno, on_delete=models.CASCADE)
     nome_professor = models.CharField(max_length=40)
     série = models.CharField(max_length=10)
     class Meta:
        verbose_name_plural = 'Gerar Listas de Presença'
     pass
     
     



     


