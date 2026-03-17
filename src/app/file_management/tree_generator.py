import os

def generate_tree(directory, indent=""):
    tree = []
    try:
        items = os.listdir(directory)
    except FileNotFoundError:
        return [f"{indent} [Directory not found: {directory}]"]
    except PermissionError:
        return [f"{indent} [Permission denied: {directory}]"]

    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = i == len(items) - 1
        marker = "└── " if is_last else "├── "
        tree.append(f"{indent}{marker}{item}")

        if os.path.isdir(path):
            new_indent = indent + ("    " if is_last else "│   ")
            tree.extend(generate_tree(path, new_indent))

    return tree

def directory_tree(directory):
    return "\n".join(generate_tree(directory))
