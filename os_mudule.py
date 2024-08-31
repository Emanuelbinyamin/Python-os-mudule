import os  # Importing the 'os' module for interacting with the operating system

# Get the current working directory (equivalent to 'pwd' in Linux or 'cd' in Windows)
curr_path = os.getcwd()
print("Current Directory:", curr_path)

# Uncomment the line below to create a single directory named 'try2'
# os.mkdir("try2")  # Creates a single directory named 'try2'

# Uncomment the line below to create a nested directory structure 'try/trip pictures/november'
# os.makedirs("try//trip pictures//november")  # Creates directories recursively

# Create a nested directory structure 'try/trip pictures/november', 
# but this time 'exist_ok=True' prevents an error if the directory already exists
os.makedirs("try//trip pictures//november", exist_ok=True)
print("Directories created successfully.")

# List the contents of the current directory (equivalent to 'ls' in Linux or 'dir' in Windows)
file_list = os.listdir(os.getcwd())
print("Directory Contents:", file_list)

# Change the current working directory to 'try' (equivalent to 'cd try')
os.chdir("try")
print("Changed Directory:", os.getcwd())
print("New Directory Contents:", os.listdir())

# Remove the directory 'trip pictures/november', but only if it's empty
os.removedirs("trip pictures//november")
print("After Removal - Current Directory:", os.getcwd())
print("After Removal - Directory Contents:", os.listdir())





