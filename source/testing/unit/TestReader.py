# Import class to test
from __init__ import NetworkReader


# Create testing instances
NetworkReaderT1 = NetworkReader('nw_data1.txt')
NetworkReaderT2 = NetworkReader('nw_data2.txt')
NetworkReaderT3 = NetworkReader('nw_data3.txt')
NetworkReaderT4 = NetworkReader('nw_data4.txt')
NetworkReaderT5 = NetworkReader('nw_data5.txt')
NetworkReaderT6 = NetworkReader('nw_data6.txt')
NetworkReaderT7 = NetworkReader(873446)
NetworkReaderT8 = NetworkReader('krjhet')

# Store instances
instances = [NetworkReaderT1, NetworkReaderT2, NetworkReaderT3, NetworkReaderT4, NetworkReaderT5, NetworkReaderT6, NetworkReaderT7, NetworkReaderT8]

# iterate through and test instances
for instance in instances:
    print(f'{str(instance)}\n')
    
    print(instance.get_nw_data())

    instance.validate_nw_data()

    print(instance._social_nw)

    print(instance.display_nw_data())
