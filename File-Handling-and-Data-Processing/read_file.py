def read_file(file_path: str):
    lines = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return lines

file_path = 'demo.txt'  
lines = read_file(file_path)
print(lines)