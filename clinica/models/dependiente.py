from django.db import models

class Dependiente(models.Model):
    titular = models.ForeignKey("clinica.Cliente", on_delete=models.DO_NOTHING, related_name='dependientes')
    dependiente = models.OneToOneField("clinica.Cliente", on_delete=models.DO_NOTHING, related_name='titular_relacion')
    
    class Meta:
        db_table = 'dependientes'
        ordering = ['pk']
        verbose_name = 'Dependiente'
        verbose_name_plural = 'Dependientes'
        permissions = [
            ['autorizar_dependientes', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_dependientes', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Titular: {self.titular} | Dependiente : {self.dependiente}"