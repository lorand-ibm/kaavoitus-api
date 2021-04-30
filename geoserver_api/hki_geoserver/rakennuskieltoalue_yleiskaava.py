from pydov.util import location
from .abstract import GeoServer_Reader_json


class Rakennuskieltoalue_yleiskaava(GeoServer_Reader_json):
    use_auth = False
    layername = 'avoindata:Rakennuskieltoalue_yleiskaavan_laatimiseksi'
    schema = {'geometry': 'GeometryCollection',
              'geometry_column': 'geom',
              'properties': {'antaja_selite': 'string',
                             'antaja_tunnus': 'string',
                             'datanomistaja': 'string',
                             'id': 'int',
                             'kunta': 'string',
                             'laatu_selite': 'string',
                             'laatu_tunnus': 'string',
                             'luontipvm': 'date',
                             'muokkauspvm': 'date',
                             'paatospvm': 'date',
                             'paattymispvm': 'date',
                             'paivitetty_tietopalveluun': 'date',
                             'rakennuskieltotunnus': 'string',
                             'tyyppi': 'string',
                             'voimaantulopvm': 'date'},
              'required': ['id']}

    def get(self, data):
        gml_polygon = self.convert_data(data)
        if not isinstance(gml_polygon, location.GmlObject):
            raise ValueError("Need GmlObject as input!")

        fields_to_retrieve = self._schema_to_fieldlist()
        num_returned, data = self.query(fields_to_retrieve,
                                        filter=gml_polygon
                                        )

        return data
