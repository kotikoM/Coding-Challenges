class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []
        self.files = []

    def add_child(self, child):
        self.children.append(child)
        self.update_size()

    def add_file(self, file):
        self.files.append(file)
        self.update_size()

    def update_size(self):
        self.size = sum(file[1] for file in self.files) + sum(child.size for child in self.children)
        if self.parent:
            self.parent.update_size()

    def get_parent(self):
        return self.parent

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def __repr__(self, level=0):
        indent = "    " * level
        result = f"{indent}📂 {self.name} {self.size}\n"

        for file in self.files:
            result += f"{indent}    📄 {file}\n"

        for child in self.children:
            result += child.__repr__(level + 1)

        return result


root = Directory('/', None)
current_dir = root
lines = open('input').read().splitlines()

pointer = 0
while pointer < len(lines):
    line = lines[pointer]
    if line.startswith('$ cd'):
        if line == '$ cd /':
            current_dir = root
        elif line == '$ cd ..':
            current_dir = current_dir.get_parent()
        else:
            current_dir = current_dir.get_child(line[5:])
            assert current_dir is not None
        pointer += 1

    elif line.startswith('$ ls'):
        pointer += 1
        while pointer < len(lines) and not lines[pointer].startswith('$'):
            line = lines[pointer]
            if line.startswith('dir'):
                current_dir.add_child(Directory(line[4:], current_dir))
            else:
                size, name = line.split()
                current_dir.add_file((name, int(size)))

            pointer += 1


sizes = [root.size]
def add_all_files(dir):
    global sizes
    if dir.children:
        for d in dir.children:
            sizes.append(d.size)

    for child in dir.children:
        add_all_files(child)

add_all_files(root)

for s in sorted(sizes):
    if root.size - s <= (70000000 - 30000000):
        print(s)
        break