from dataclasses import dataclass

@dataclass
class Location:
    location:str
    latitude:float
    longitude:float

    def __hash__(self):
        return hash(self.location)

    def __eq__(self, other):
        return self.location == other.location

    def __str__(self):
        pass