from django.contrib import admin
from .models import Aluno
from .models import Servidor
from .models import Notificacao
from .models import SelecionarPresencaseFaltas
from .models import Cargo
from .models import Adicionar_Justificativa_de_Falta
from .models import GerarDeclaracaoEstudantil
from .models import GerarListasDePresenca



# Register your models here.

admin.site.register(Aluno)
admin.site.register(Servidor)
admin.site.register(Notificacao)
admin.site.register(SelecionarPresencaseFaltas)
admin.site.register(Cargo)
admin.site.register(Adicionar_Justificativa_de_Falta)
admin.site.register(GerarDeclaracaoEstudantil)
admin.site.register(GerarListasDePresenca)


