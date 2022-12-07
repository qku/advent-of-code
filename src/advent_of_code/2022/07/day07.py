def get_dir(_file_tree, _path):
    _current_dir = _file_tree
    for _k in _path:
        _current_dir = _current_dir[_k]
    return _current_dir


def parse_ls(line_it, _dir):
    line = next(line_it)
    while not line.startswith('$'):
        x, name = line.split()
        if x == 'dir':
            _dir[name] = {}
        else:
            size = int(x)
            _dir[name] = size
        line = next(line_it)
    return line


def dir_size(_dir):
    _size = 0
    for key, value in _dir.items():
        if type(value) == dict:
            _size += dir_size(value)
        else:
            _size += int(value)
    return _size


def list_dir_sizes(_dir):
    _size_list = []
    for key, value in _dir.items():
        if type(value) == dict:
            _size_list.append(dir_size(value))
            _size_list += list_dir_sizes(value)
    return _size_list


file = 'input.txt'
# file = 'text_input.txt'
with open(file) as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
lines = iter(lines)

file_tree = {'/': {}}
current_path = []

next_command = next(lines)
try:
    while True:
        # print(file_tree)
        # print(current_path)
        # print(next_command)
        if next_command == '$ cd ..':
            current_path.pop()
            next_command = next(lines)
        elif next_command.startswith('$ cd'):
            current_path.append(next_command.split()[-1])
            next_command = next(lines)
        elif next_command == '$ ls':
            current_dir = get_dir(file_tree, current_path)
            next_command = parse_ls(lines, current_dir)
        else:
            print(next_command)
            raise ValueError
except StopIteration:
    pass

print(file_tree)

dir_sizes = list_dir_sizes(file_tree)

# part I
sum_of_small_dirs = 0
for i in dir_sizes:
    if i < 100000:
        sum_of_small_dirs += i
print(sum_of_small_dirs)

# part II
total_space = 70000000
required_unused_space = 30000000
used_space = max(dir_sizes)
unused_space = total_space - used_space
min_delete_size = required_unused_space - total_space + used_space
print(f'Trying to find folder with a size of at least {min_delete_size} to delete...')

candidate_size = total_space
for i in dir_sizes:
    if min_delete_size <= i < candidate_size:
        candidate_size = i
print(f'Smallest possible folder of size {candidate_size} found.')
