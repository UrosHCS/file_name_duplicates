import os

names = {}

file_number = 1
file_name_prefix = 'results'
file_created = False
while not file_created:
    file_name = file_name_prefix + str(file_number)
    if (not os.path.isfile(file_name)):
        out = open(file_name, 'w')
        file_created = True
        print('Writing to file ', file_name)
    else:
        file_number += 1

directory_to_walk = '.'
file_names_to_skip = ['Thumbs.db']

for root, dirs, files in os.walk(directory_to_walk):
    for file_name in files:
        if (file_name not in file_names_to_skip):
            if file_name in names:
                names[file_name].append(root)
            else:
                names[file_name] = [root]

for name, dirs in names.items():
    if len(dirs) > 1:
        out.write(name + ':\n')
        for dir in dirs:
            out.write(dir + "\\" + name + '\n')
        out.write('\n')
