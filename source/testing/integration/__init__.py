from colorama import Fore, Style
from source.classes.custom_exceptions import FileConsistencyError


class NetworkReader:
    def __init__(self, filename: str):
        self._filename = filename
        self._num_of_users = None
        self._social_nw = {}

    def get_nw_data(self):
        """
        It reads the file line by line, and for each line, it splits the line into parts, and then adds the parts to the
        social network
        """
        # Reading the first line of the file and assigning it to the variable `self._num_of_users`
        try:
            with open(self._filename, 'r') as f:
                self._num_of_users = f.readline().strip()
                print(f'Total users: {self._num_of_users}')

                users = []

                # Reading the file line by line, and for each line, it splits the line into parts, and then adds the
                # parts to the social network.
                for line in f:
                    parts = line.strip().split()

                    if len(parts) == 2:
                        if parts[0] not in self._social_nw:
                            self._social_nw[parts[0]] = []
                        if parts[1] not in self._social_nw:
                            self._social_nw[parts[1]] = []
                        self._social_nw[parts[0]].append(parts[1])
                        self._social_nw[parts[1]].append(parts[0])
                    # Adding the parts to the list `users`.
                    users.extend(parts)

                # Checking if there is any user in the list `users` that is not in the social network. If there is, then
                # it adds that user to the social network.
                for user in set(users):
                    if user not in self._social_nw:
                        self._social_nw[user] = []
        except OSError as e:
            print(f'Failed with exception {e}, pleasse try again')
            return False

    def validate_nw_data(self):
        """
        It checks if the friend of a friend is also a friend of the original person, if not then it raises an exception
        """
        for key, value in self._social_nw.items():
            for friend in value:
                if key not in self._social_nw[friend]:
                    raise FileConsistencyError(f'File name: {self._filename}, '
                                               f'Inconsistent network: {key} is friends with {friend}, '
                                               f'but {friend} is not friends with {key}.')
                else:
                    print('Network is consistent.')

    def display_nw_data(self):
        """
        It takes the dictionary of the social network and returns a string of the social network in the format of:

        :return: The result is a string that contains the social network data.
        """
        result = ''
        for key, value in self._social_nw.items():
            value_str = ', '.join(value)
            result += f'{Fore.GREEN}{key} -> {Fore.RED}{value_str}\n{Style.RESET_ALL}'
        return result


class FriendHandler:
    def __init__(self, friend_data: dict):
        self.friend_data = friend_data
        self._common_friends = {}

    def common_count(self):
        common_friends = {}
        for name1, friends1 in self.friend_data.items():
            for name2 in self.friend_data:
                if name1 != name2:
                    common = set(friends1).intersection(self.friend_data[name2])
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
        if name in self.friend_data:
            mutual_friends = {}
            for friend in self.friend_data:
                if friend != name:
                    mutual_friends[friend] = len(set(self.friend_data[friend]) & set(self.friend_data[name]))
            mutual_friends = dict(sorted(mutual_friends.items(), key=lambda item: item[1], reverse=True))
            for friend, common_friends in mutual_friends.items():
                if common_friends > 0:
                    return f'{Fore.GREEN}The recommended friend for {Fore.RED}{name} {Fore.GREEN}is ' \
                           f'{Fore.RED}{friend}{Style.RESET_ALL}'
                else:
                    return f'{Fore.RED}{name} has no friends to recommend.{Style.RESET_ALL}'
        else:
            return f'{Fore.RED}{name} is not in the network.{Style.RESET_ALL}'


class Analyser:
    def __init__(self, data: dict):
        self.data = data

    def calc_friend_total(self, user):
        friends = self.data.get(user)
        if friends is not None:
            total_friends = len(friends)
            return f'{Fore.GREEN}{user} has {str(total_friends)} ' \
                   f'{"friends" if len(friends) > 1 or len(friends) == 0 else "friend"}{Style.RESET_ALL}'
        else:
            return f'{Fore.RED} User not found{Style.RESET_ALL}'

    def least_friends(self):
        least_friends = float('inf')
        users_with_least_friends = []
        for user, friends in self.data.items():
            num_friends = len(friends)
            if num_friends < least_friends:
                least_friends = num_friends
                users_with_least_friends = [user]
            elif num_friends == least_friends:
                users_with_least_friends.append(user)

        results = ''
        for user in users_with_least_friends:
            results += f"{Fore.GREEN}{user}{Style.RESET_ALL}\n"

        return results

    def direct_relationships(self, user):
        friends = self.data.get(user)
        if friends is not None:
            if friends:
                return f'{Fore.GREEN}{", ".join(friends)}{Style.RESET_ALL}'
            else:
                return f'{Fore.RED}This user has no direct relationships{Style.RESET_ALL}'
        else:
            return f'{Fore.RED}User not found{Style.RESET_ALL}'

    def indirect_relationships(self):
        indirect_friends = {}
        for user, friends in self.data.items():
            if not friends:
                indirect_friends[user] = ""
            else:
                indirect_friends[user] = set(
                    friend for friend_list in (self.data.get(friend, []) for friend in friends) for friend in
                    friend_list
                ) - set(friends) - {user}

        output = ""
        for user, friends in indirect_friends.items():
            output += f'{Fore.GREEN}{user} -> {friends}{Style.RESET_ALL}\n'
        return output


class FileConsistencyError(Exception):
    """
    Raised when a files contents is incosistent with the desired data
    """
    pass
