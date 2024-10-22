from abc import ABC, abstractmethod
import unittest


class RadioStation:
    def __init__(self, frequency):
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def __str__(self):
        return f"RadioStation: {self.frequency}"


class StationList:
    def __init__(self):
        self.stations = []
        self.counter = 0

    def add_station(self, station):
        self.stations.append(station)

    def remove_station(self, to_remove):
        self.stations = [station for station in self.stations if station.get_frequency() != to_remove]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.stations):
            station = self.stations[self.counter]
            self.counter += 1
            return station
        else:
            raise StopIteration
        
    def count(self):
        return len(self.stations)
    
    def current(self):
        return self.stations[self.counter]
    
    def key(self):
        return self.counter

    def next(self):
        self.counter += 1

    def rewind(self):
        self.counter = 0

    def valid(self):
        return self.counter < len(self.stations)



class TestIterator(unittest.TestCase):
    def test_iterator(self):
        station_list = StationList()
        station_list.add_station(RadioStation(89))
        station_list.add_station(RadioStation(101))
        station_list.add_station(RadioStation(102))

        self.assertEqual(station_list.count(), 3)
        self.assertEqual(station_list.current().get_frequency(), 89)
        self.assertEqual(station_list.key(), 0)
        station_list.next()
        self.assertEqual(station_list.current().get_frequency(), 101)
        self.assertEqual(station_list.key(), 1)
        station_list.rewind()
        self.assertEqual(station_list.current().get_frequency(), 89)
        self.assertEqual(station_list.key(), 1)
        self.assertTrue(station_list.valid())

if __name__ == "__main__":
    unittest.main()
