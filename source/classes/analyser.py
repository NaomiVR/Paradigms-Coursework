from colorama import Fore, Style


class Analyser:
    def __init__(self, data: dict):
        self.data = data

    def calc_friend_total(self, user):
        """
        It takes a user as an argument, checks if the user exists in the data dictionary, and if so, returns the number
        of friends the user has

        :param user: The user whose friends we want to count
        :return: The number of friends a user has.
        """
        friends = self.data.get(user)
        if friends is not None:
            total_friends = len(friends)
            return f'{Fore.GREEN}{user} has {str(total_friends)} ' \
                   f'{"friends" if len(friends) > 1 or len(friends) == 0 else "friend"}{Style.RESET_ALL}'
        else:
            return f'{Fore.RED} User not found{Style.RESET_ALL}'

    def least_friends(self):
        """
        We loop through the data, keeping track of the number of friends each user has, and the user with the least
        friends.

        If we find a user with fewer friends than the current user with the least friends, we update the user with the
        least friends.

        If we find a user with the same number of friends as the current user with the least friends, we add that user
        to the list of users with the least friends.

        Finally, we return a string with the users with the least friends.

        :return: A list of users with the least number of friends.
        """
        least_friends = float('inf')
        users_with_least_friends = []
        # Looping through the data, keeping track of the number of friends each user has, and the user with the least
        # friends.
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
        """
        If the user exists, return a list of their friends, otherwise return an error message

        :param user: The user whose direct relationships we want to see
        :return: A string with the direct relationships of the user.
        """
        friends = self.data.get(user)
        if friends is not None:
            if friends:
                return f'{Fore.GREEN}{", ".join(friends)}{Style.RESET_ALL}'
            else:
                return f'{Fore.RED}This user has no direct relationships{Style.RESET_ALL}'
        else:
            return f'{Fore.RED}User not found{Style.RESET_ALL}'

    def indirect_relationships(self):
        """
        For each user, get the list of their friends, and then for each of those friends, get the list of their friends,
        and then remove the user's friends and the user from the list

        :return: A dictionary of users and their indirect friends.
        """
        indirect_friends = {}
        # Looping through the data, and for each user, it is getting the list of their friends.
        for user, friends in self.data.items():
            if not friends:
                indirect_friends[user] = ""
            else:
                # Getting the list of friends for each of the user's friends, and then removing the user's friends and
                # the user from the list.
                indirect_friends[user] = set(
                    friend for friend_list in (self.data.get(friend, []) for friend in friends) for friend in
                    friend_list
                ) - set(friends) - {user}

        output = ""
        for user, friends in indirect_friends.items():
            output += f'{Fore.GREEN}{user} -> {friends}{Style.RESET_ALL}\n'
        return output
