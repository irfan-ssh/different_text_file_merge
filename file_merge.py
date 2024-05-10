def merge_files(file_paths, output_path):
    with open(output_path, 'w') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r') as input_file:
                links = input_file.readlines()
                output_file.writelines(links)

if __name__ == "__main__":
    file_paths = ["file.txt", "file1.txt"]
    output_path = "merge.txt"
    merge_files(file_paths, output_path)
    print("Files merged successfully!")
