# Import network reader to test incorrect validation
from __init__ import NetworkReader


# Incorrect data
t1 = {'Adam': ['Bob'], 'Bob': ['Amir', 'Mia'], 'Amir': ['Bob', 'Mia'], 'Mia': ['Bob', 'Amir'], 'Chris': ['Zia'], 'Zia': ['Chris'], 'Liz': []}

# Instance
NetworkReader = NetworkReader('nw_data1.txt')

# Set instance variable to test data
NetworkReader._social_nw = t1

print(NetworkReader.validate_nw_data())
