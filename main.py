# Import internal functions
from source.classes.analyser import Analyser
from source.classes.friend_handler import FriendHandler
from source.classes.network_reader import NetworkReader

# Import external libraries
import os
from colorama import Style


def clear():
    """
    If the operating system is Windows, then clear the screen using the cls command. Otherwise, if the operating system
    is not Windows, then clear the screen using the clear command
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Main function loop
def main():
    with open('application_message.txt', 'r') as f:
        for line in f:
            print(line.strip())

    while True:
        file_name = input('Please enter the file name: ')
        file_path = os.path.abspath(file_name)
        try:
            network_reader = NetworkReader(file_path)
            if network_reader.get_nw_data() is False:
                main()
            network_reader.validate_nw_data()
            print(network_reader._social_nw)
            print('File loaded successfully!')

            friend_handler = FriendHandler(network_reader._social_nw)
            analyser = Analyser(network_reader._social_nw)

            while True:
                print(Style.RESET_ALL)
                print('\n')
                print('Please select an option')
                print('1. Display the social network')
                print('2. Get common friend count')
                print('3. Recommend a friend')
                print('4. Display number of friends for a given user')
                print('5. Show user with least number of friends/ no friends')
                print('6. Show all relationships of a given user')
                print('7. Show indirect relationships between users')
                print('8. Exit')
                choice = int(input('Option: '))
                if choice == 1:
                    clear()
                    print(network_reader.display_nw_data())
                elif choice == 2:
                    clear()
                    print(friend_handler.common_count())
                elif choice == 3:
                    clear()
                    name = input('Enter the name of the user: ')
                    print(friend_handler.recommend(name))
                elif choice == 4:
                    clear()
                    name = input('Enter the name of the user: ')
                    print(analyser.calc_friend_total(name))
                elif choice == 5:
                    clear()
                    print(analyser.least_friends())
                elif choice == 6:
                    clear()
                    name = input('Enter the name of the user: ')
                    print(analyser.direct_relationships(name))
                elif choice == 7:
                    clear()
                    print(analyser.indirect_relationships())
                elif choice == 8:
                    clear()
                    print('Thank you, goodbye!')
                    exit()
                else:
                    clear()
                    print('Invalid option, please try again.')
            break
        except FileNotFoundError:
            print('File not found, please try again.')
            choice = input('Do you want to try again? (y/n)').strip().lower()
            if choice == 'n':
                print('Thank you, goodbye!')
                break
            elif choice == 'y':
                continue
            else:
                print('Invalid option, retrying anyway')


if __name__ == '__main__':
    main()
