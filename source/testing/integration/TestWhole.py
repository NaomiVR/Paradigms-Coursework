# Import all classes
from __init__ import NetworkReader, FriendHandler, Analyser

# Create testing instances
NetworkReaderT1 = NetworkReader('nw_data1.txt')
NetworkReaderT2 = NetworkReader('nw_data2.txt')
NetworkReaderT3 = NetworkReader('nw_data3.txt')
NetworkReaderT4 = NetworkReader('nw_data4.txt')
NetworkReaderT5 = NetworkReader('nw_data5.txt')
NetworkReaderT6 = NetworkReader('nw_data6.txt')

# Store instances
instances = [NetworkReaderT1, NetworkReaderT2, NetworkReaderT3, NetworkReaderT4, NetworkReaderT5, NetworkReaderT6]

# iterate through and test instances
for NRinstance in instances:
    # Network reader testing
    print('NOW TESTING MAIN READER INSTANCE')

    print(NRinstance.get_nw_data())

    NRinstance.validate_nw_data()

    print(NRinstance._social_nw)

    print(NRinstance.display_nw_data())

    # Friend handler testing
    print('NOW TESTING FRIEND HANDLER')
    FHinstance = FriendHandler(NRinstance._social_nw)

    print(FHinstance.common_count())

    for name in NRinstance._social_nw.keys():
        print(FHinstance.recommend(name))


    # Analyser testing
    print('NOW TESTING ANALYSER')
    ANinstance = Analyser(NRinstance._social_nw)

    for user in NRinstance._social_nw.keys():
        print(ANinstance.calc_friend_total(user))

    print(ANinstance.least_friends())

    for user1 in NRinstance._social_nw.keys():
        print(ANinstance.direct_relationships(user1))

    print(ANinstance.indirect_relationships())