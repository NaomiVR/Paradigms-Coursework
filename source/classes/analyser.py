from colorama import Fore, Style


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
