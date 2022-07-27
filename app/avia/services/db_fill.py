import numpy as np
import pandas as pd

from avia.models import AirportType, Airport

def refill_db_avia_data(file_path):
  df = pd.read_csv(file_path, delimiter=',')
  df = df.replace({np.nan: None})

  airports_types = set(df['type']) - set(AirportType.objects.values_list('title', flat=True)) - {None}

  AirportType.objects.bulk_create([
    AirportType(
      title=airport_type
    ) for airport_type in airports_types
  ])

  airport_types = {**dict(AirportType.objects.values_list('title', 'id')), **{None:None}}

  Airport.objects.all().delete()

  Airport.objects.bulk_create([
    Airport(
      ident=airport.ident,
      local_code=airport.local_code,
      name=airport.name,
      type_id=airport_types[airport.type],
    ) for airport in df.itertuples()
  ])
