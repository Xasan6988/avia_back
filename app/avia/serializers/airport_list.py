
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from avia.models import Airport


class AirportListElemetSerializer(ModelSerializer):
    type = StringRelatedField()

    class Meta:
        model = Airport
        fields = (
            'id',
            "name",
            "ident",
            "local_code",
            "type",
        )
