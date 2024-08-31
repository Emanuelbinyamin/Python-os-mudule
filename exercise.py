import os  # Importing the 'os' module for operating system interactions

# Create a new directory named 'exercise_dir' in the current directory
os.mkdir('exercise_dir')
print("Directory 'exercise_dir' created.")

# Change the current working directory to 'exercise_dir'
os.chdir('exercise_dir')
print("Changed to Directory:", os.getcwd())

# Create an empty text file named 'example.txt' in 'exercise_dir'
with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # Writing some content to the file
print("File 'example.txt' created and content written.")

# Rename the file from 'example.txt' to 'renamed_example.txt'
os.rename('example.txt', 'renamed_example.txt')
print("File - 'example.txt', renamed to 'renamed_example.txt'.")

# Get the size of 'renamed_example.txt' in bytes
file_size = os.path.getsize('renamed_example.txt')
print(f"Size of 'renamed_example.txt': {file_size} bytes")

# List all files and directories in the current directory
current_files = os.listdir()
print("Current Directory Contents:", current_files)

# Get the absolute path of 'renamed_example.txt'
file_path = os.path.abspath('renamed_example.txt')
print(f"Absolute Path of 'renamed_example.txt': {file_path}")

# Check if 'renamed_example.txt' exists in the directory
file_exists = os.path.exists('renamed_example.txt')
print(f"Does 'renamed_example.txt' exist?: {file_exists}")

# Remove the file 'renamed_example.txt'
os.remove('renamed_example.txt')
print("File 'renamed_example.txt' removed.")

# Move up one directory level (equivalent to 'cd ..')
os.chdir('..')
print("Moved up one directory level:", os.getcwd())

# Remove the directory 'exercise_dir'
os.rmdir('exercise_dir')
print("Directory 'exercise_dir' removed.")
print("Does 'exercise_dir' exist?:" , os.path.exists("exercise_dir"))
command_output = os.system('dir')
print("Command 'ls' executed with output:", command_output)# like writting dir in the cmd/