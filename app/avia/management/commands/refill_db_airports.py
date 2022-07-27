from django.core.management import BaseCommand

from avia.services.db_fill import refill_db_avia_data

class Command(BaseCommand):
  help = 'Заполнить БД аэропортов'

  def handle(self, *args, **options):
    self.stdout.write('Заполнение данных', ending='\r')
    refill_db_avia_data('storage/airport-codes.csv')
    self.stdout.write('Заполнение данных - готово')


