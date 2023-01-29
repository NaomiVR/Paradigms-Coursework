from colorama import Fore, Style


class FriendHandler:
    def __init__(self, friend_data: dict):
        self.friend_data = friend_data
        self._common_friends = {}

    def common_count(self):
        """
        For each pair of friends, find the number of common friends they have and store it in a dictionary

        :return: A string with the name of the person and the number of common friends they have with each other person.
        """
        common_friends = {}
        # Checking if there are any common friends between two people, and if there are, it adds the
        # number of common friends to the dictionary. If there are no common friends, it adds 0 to the
        # dictionary.
        for name1, friends1 in self.friend_data.items():
            for name2 in self.friend_data:
                if name1 != name2:
                    common = set(friends1).intersection(self.friend_data[name2])
                    # Checking if there are any common friends between two people, and if there are, it adds the
                    # number of common friends to the dictionary. If there are no common friends, it adds 0 to the
                    # dictionary.
                    if common:
                        count = len(common)
                        self._common_friends[(name1, name2)] = (count, common)
                        common_friends[name1] = common_friends.get(name1, []) + [count]
                        common_friends[name2] = common_friends.get(name2, []) + [count]
                    else:
                        common_friends[name1] = common_friends.get(name1, []) + [0]
                        common_friends[name2] = common_friends.get(name2, []) + [0]

        result = ''
        for name, counts in common_friends.items():
            result += f'{Fore.GREEN}{name} -> {Fore.RED}{counts}{Style.RESET_ALL}\n'

        return result

    def recommend(self, name):
        """
        It takes a name as an argument, checks if the name is in the network, and if it is, it creates a dictionary of
        all the friends of the name, and the number of mutual friends they have with the name. It then sorts the
        dictionary by the number of mutual friends, and returns the friend with the most mutual friends

        :param name: The name of the person you want to recommend a friend for
        :return: a string with the recommended friend for the given name.
        """
        # Checking if the name is in the network, and if it is, it creates a dictionary of all the friends of the name,
        # and the number of mutual friends they have with the name.
        if name in self.friend_data:
            mutual_friends = {}
            for friend in self.friend_data:
                if friend != name:
                    mutual_friends[friend] = len(set(self.friend_data[friend]) & set(self.friend_data[name]))
            # It sorts the dictionary by the number of mutual friends, and returns the friend with the most mutual
            # friends.
            mutual_friends = dict(sorted(mutual_friends.items(), key=lambda item: item[1], reverse=True))
            for friend, common_friends in mutual_friends.items():
                if common_friends > 0:
                    return f'{Fore.GREEN}The recommended friend for {Fore.RED}{name} {Fore.GREEN}is ' \
                           f'{Fore.RED}{friend}{Style.RESET_ALL}'
                else:
                    return f'{Fore.RED}{name} has no friends to recommend.{Style.RESET_ALL}'
        else:
            return f'{Fore.RED}{name} is not in the network.{Style.RESET_ALL}'
