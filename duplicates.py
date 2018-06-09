import os
import math
import sys

# One argument can be passed and it is set as directory_to_walk
try:
    directory_to_walk = sys.argv[1]
except IndexError:
    directory_to_walk = '.'

print('Walking through: ' + directory_to_walk)

# Stores all needed file names
names = {}

# Make a new empty file
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

# Iterate through all files in all folders
file_names_to_skip = []

for root, dirs, files in os.walk(directory_to_walk):
    for file_name in files:
        if (file_name not in file_names_to_skip):
            if file_name in names:
                names[file_name].append(root)
            else:
                names[file_name] = [root]

# Print files that are similar in size
for name, dirs in names.items():
    dirs_len = len(dirs)

    if dirs_len > 1:
        # Get all file sizes
        file_sizes = []
        for dir in dirs:
            full_path = os.path.join(dir, name)
            kilobytes = os.path.getsize(full_path)
            file_sizes.append(kilobytes)

        # If all sizes are different then no need to print the file names
        same_sizes = False
        # file_sizes_len is same as dirs_len
        for i in range(0, dirs_len - 1):
            for j in range(i + 1, dirs_len):
                avg_size = file_sizes[i]/2 + file_sizes[j]/2
                abs_diff = math.fabs(file_sizes[i] - file_sizes[j])
                relative_diff = 100 * abs_diff/avg_size
                if relative_diff < 1:
                    same_sizes = True

        if same_sizes:
            out.write(name + ':\n')
            for dir in dirs:
                full_path = os.path.join(dir, name)
                kilobytes = os.path.getsize(full_path)
                out.write(full_path + ' - ' + str(kilobytes) + '\n')
            out.write('\n')
