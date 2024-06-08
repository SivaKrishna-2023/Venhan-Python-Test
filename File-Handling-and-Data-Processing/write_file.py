from typing import List

def write_file(file_path: str, lines: List[str]) -> None:
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


file_path = 'output.txt'
lines = ['Line 1', 'Line 2', 'Line 3']
write_file(file_path, lines)