def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a') as f:
        f.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", encoding="utf-8") as f:
        open_content = f.read()
    return open_content
