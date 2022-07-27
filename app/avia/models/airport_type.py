from django.db.models import Model, CharField

class AirportType(Model):
  title = CharField('Наименование', max_length=255)

  class Meta:
    verbose_name = 'Вид аэропорта'
    verbose_name_plural = 'Виды аэропортов'


  def __str__(self):
    return self.title
