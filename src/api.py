import os
import csv
import rich
import time

from .aircraft import Aircraft
from .airport import Airport

class API:
    def __init__(self):
        self._success('started api')
        self.load_aircrafts()
        self.load_airports()
        print(self.airport_icao_hashtable['EDDF'])

    def _success(self, text):
        rich.print(f'[green]{time.time()} INFO: {text}[/]')

    def _path(self, *path):
        return os.path.join(os.path.dirname(__file__), *path)

    def load_aircrafts(self) -> bool:
        with open(self._path('data', 'aircrafts.csv'), 'r') as f:
            self.aircrafts = [Aircraft(*r) for r in csv.reader(f)]
        
        self.aircraft_shortname_hashtable = {}
        for i, a in enumerate(self.aircrafts):
            self.aircraft_shortname_hashtable[a.a_shortname] = i

    def load_airports(self) -> bool:
        with open(self._path('data', 'airports.csv'), 'r') as f:
            self.airports = [Airport(*r) for r in csv.reader(f)]
            self._success('finished loading airports!')

        self.airport_icao_hashtable = {}
        self.airport_iata_hashtable = {}
        self.airport_id_hashtable = {}
        for i, a in enumerate(self.airports):
            self.airport_icao_hashtable[a.icao] = i
            self.airport_iata_hashtable[a.iata] = i
            self.airport_id_hashtable[a.id] = i