import os

def combine_paths(directory, folder_name):
    """Combine a directory and a folder name into a full path."""
    return os.path.join(directory, folder_name)

def is_file(directory, element):
    """Check if the given element in a directory is a file."""
    return os.path.isfile(combine_paths(directory, element))

def save(string):
    """Show the string on the console and write it in text file"""
    print(string)
    with open("Summary.txt","a", encoding="utf-8") as file:
        file.write(string+"\n")

def display_tree(directory, prefix=""):
    """Recursively display the directory tree structure."""
    try:
        items = sorted(os.listdir(directory), key=lambda x: (not is_file(directory, x), x.lower()))
    except FileNotFoundError:
        print(f"{prefix}Directory not found: {directory}")
        return

    for i, item in enumerate(items):
        full_path = combine_paths(directory, item)
        is_last = (i == len(items) - 1)

        # Print the current item
        branch = "└──" if is_last else "├──"
        save(f"{prefix}{branch} {item}")

        # Recur if it's a directory
        if not is_file(directory, item):
            next_prefix = prefix + ("    " if is_last else "│   ")
            display_tree(full_path, next_prefix)

def display_codes(directory):
    """Display the content of all files in the directory and subdirectories."""
    try:
        items = sorted(os.listdir(directory), key=lambda x: (not is_file(directory, x), x.lower()))
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return

    for item in items:
        full_path = combine_paths(directory, item)

        if is_file(directory, item):
            try:
                with open(full_path, "r", encoding="utf-8") as file:
                    save(f"\n# {full_path[full_path.index(os.path.basename(root_dir)):]}")
                    save(file.read())
                    save("\n" + "-" * 80 + "\n")
            except Exception as e:
                print(f"Could not read file {full_path}: {e}")
        else:
            display_codes(full_path)

if __name__ == "__main__":
    # Prompt the user for the root directory
    root_dir = input("Enter the root directory path: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.isdir(root_dir):
        print(f"Invalid directory: {root_dir}")
    else:
        with open("Summary.txt","w", encoding="utf-8") as file:pass # reset the Summary file
        print(f"\nDirectory Tree for: {os.path.basename(root_dir)}")
        display_tree(root_dir)

        print("\nDisplaying file contents:\n")
        display_codes(root_dir)
