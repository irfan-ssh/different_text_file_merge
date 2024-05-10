import os
directory_path_name = input("Enter the directory path: ")
def merge_files_in_directory(directory_path, output_path):
    with open(output_path, 'w') as output_file:
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as input_file:
                    links = input_file.readlines()
                    output_file.writelines(links)
    print("Files merged successfully!")

if __name__ == "__main__":
    directory_path = directory_path_name
    output_path = "merge.txt"
    merge_files_in_directory(directory_path, output_path)
