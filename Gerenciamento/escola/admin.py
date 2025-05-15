from django.contrib import admin
from .models import (Usuario,
                     Disciplina,
                     ReservaAmbiente
                     )

admin.site.register(Usuario)
admin.site.register(Disciplina)
admin.site.register(ReservaAmbiente)