from django.db import models

class Gasto(models.Model):
    cliente = models.ForeignKey('clinica.Cliente', on_delete=models.DO_NOTHING, related_name='gastos')
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    
    class Meta:
        db_table = 'gastos'
        ordering = ['pk']
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        permissions = [
            ['autorizar_gastos', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_gastos', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Paciente: {self.cliente} | Concepto : {self.concepto}"