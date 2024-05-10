import os

def merge_files_in_directory(input_directory, output_directory):
    output_path = os.path.join(output_directory, "merge.txt")
    with open(output_path, 'w') as output_file:
        for file_name in os.listdir(input_directory):
            file_path = os.path.join(input_directory, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as input_file:
                    links = input_file.readlines()
                    for link in links:  
                        output_file.write(link.strip() + "\n")  # Space of between every line
                        output_file.write("\n")
    print("Files merged successfully!")

if __name__ == "__main__":
    input_directory = input("Enter the input Folder path: ")
    output_directory = input("Enter the output Folder path: ")
    
    merge_files_in_directory(input_directory, output_directory)