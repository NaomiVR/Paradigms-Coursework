import random

number_of_lines = int(input('Number of lines: '))

file_path1 = "firstnames.txt"
file_path2 = "new_gen.txt"

unique_names = []
unique_names_2 = []

with open(file_path1, 'r') as f:
    lines = f.read().splitlines()
    for q in range(0, number_of_lines):
        name_1 = random.choice(lines)
        unique_names.append(name_1)

    for w in range(0, number_of_lines):
        float_value = random.random()
        if float_value >= 0.3:
            name_2 = random.choice(unique_names)

            if name_2 == unique_names[w]:
                name_2 = random.choice(unique_names)
                unique_names_2.append(name_2)
            else:
                unique_names_2.append(name_2)
        else:
            unique_names_2.append('')
    name_list = list(map(lambda x, y: (x, y), unique_names, unique_names_2))


with open(file_path2, 'w') as z:
    for elem in name_list:
        name1, name2 = elem
        z.write(f'{name1} {name2}\n')


