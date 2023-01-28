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
        with open(self._filename, 'r') as f:
            self._num_of_users = f.readline().strip()
            print(f'Total users: {self._num_of_users}')

            users = []

            for line in f:
                parts = line.strip().split()

                if len(parts) == 2:
                    if parts[0] not in self._social_nw:
                        self._social_nw[parts[0]] = []
                    if parts[1] not in self._social_nw:
                        self._social_nw[parts[1]] = []
                    self._social_nw[parts[0]].append(parts[1])
                    self._social_nw[parts[1]].append(parts[0])
                users.extend(parts)

            for user in set(users):
                if user not in self._social_nw:
                    self._social_nw[user] = []

    def validate_nw_data(self):
        """
        It checks if the friend of a friend is also a friend of the original person
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
