from django.db import models

class Aseguranza(models.Model):
    """
    Modelo de Aseguranza
    """  
    nombre = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Nombre de la aseguranza')
    
    class Meta:
        db_table = 'aseguranzas'
        ordering = ['pk']
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        permissions = [
            ['autorizar_aseguranza', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_aseguranza', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre: {self.nombre}  "
