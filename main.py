class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = {}

    def add(self, path, name):
        node = self._get_node(path)
        if node is not None:
            node.subdirs[name] = Directory(name)
        else:
            print(f"Path '{path}' not found.")

    def delete(self, path):
        parent_path, name = path.rsplit('/', 1) if '/' in path else ('', path)
        parent = self._get_node(parent_path)
        if parent and name in parent.subdirs:
            del parent.subdirs[name]
        else:
            print(f"Directory '{path}' not found.")

    def _get_node(self, path):
        node = self
        for part in path.split('/') if path else []:
            node = node.subdirs.get(part)
            if node is None:
                return None
        return node

    def show(self, level=0):
        print("  " * level + self.name)
        for sub in sorted(self.subdirs):
            self.subdirs[sub].show(level + 1)

# Create the root directory
tree = Directory("Pictures")

tree.add("Pictures", "Saved Pictures")
tree.add("Pictures/Saved Pictures", "Web Images")
tree.add("Pictures/Saved Pictures/Web Images", "Chrome")
tree.add("Pictures/Saved Pictures/Web Images", "Opera")
tree.add("Pictures/Saved Pictures/Web Images", "Firefox")
tree.add("Pictures", "Screenshots")
tree.add("Pictures", "Camera Roll")
tree.add("Pictures/Camera Roll", "2025")
tree.add("Pictures/Camera Roll", "2024")
tree.add("Pictures/Camera Roll", "2023")

tree.show()

# Delete a directory
tree.delete("Pictures/Saved Pictures/Web Images/Opera")
print("\nAfter Deleting 'Opera':")
tree.show()
