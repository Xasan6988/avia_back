from django.db.models import Model, CharField, ForeignKey, CASCADE

class Airport(Model):
  ident = CharField('Идентификатор', max_length=10, unique=True)
  local_code = CharField('Код', max_length=10, blank=True, null=True)
  name = CharField('Наименование', max_length=255)

  type = ForeignKey('avia.AirportType', verbose_name='Тип аэропорта', on_delete=CASCADE, related_name='airport')

  class Meta:
    verbose_name = 'аэропорт'
    verbose_name_plural = 'аэропорты'

  def __str__(self):
    return self.name
