import os  # Importing the 'os' module for operating system interactions

#**********************************************************************************************************************************************#
#**********************************************************************************************************************************************#

# 1. How can you retrieve the environment variables on your system? - Useful for getting or setting system-wide variables.
env_variables = os.environ
print("Environment Variables:", env_variables)
print("-" * 40)

#**********************************************************************************************************************************************#

# 2. How do you add or modify an environment variable?
os.environ['MY_VAR'] = 'my_value'#This line creates a new environment variable named MY_VAR with the value my_value.
print("New Environment Variable - MY_VAR:", os.environ['MY_VAR']) 
print("-" * 40)

#**********************************************************************************************************************************************#

# 3. How can you check the current process ID? - useful for process management.
process_id = os.getpid()
print("Current Process ID:", process_id)
print("-" * 40)

#**********************************************************************************************************************************************#

# 4. How do you get the parent process ID of the current process?
# When a process starts another process, the original process becomes the parent.
# The Parent Process ID (PPID) is the ID of the process that created (or spawned) the current process.
parent_process_id = os.getppid()
print("Parent Process ID:", parent_process_id)
# The PPID is useful for understanding the process hierarchy.
# For example, if your Python script is run from a command line,
# the command line shell (like cmd.exe on Windows \ bash on Linux) would be the parent process.
print("-" * 40)

#**********************************************************************************************************************************************#

# 5. How can you create a pipeline of commands using `os.popen()` on Windows?
# A pipeline allows you to connect the output of one command directly to the input of another.
stream = os.popen('echo Hello World') # opens a pipe to or from a command.
# It allows you to execute a shell command and connect to its standard input/output.

output = stream.read()# The stream object is a file-like object returned by os.popen() that contains the output of the command.
print("Output of Command 'echo Hello World':", output.strip())
# The strip() method is used to remove any leading or trailing whitespace (including newline characters) from the output.
#  This ensures that the printed output is clean and without unnecessary spaces or line breaks.

# **********************************************************************************************************************************************#

# 6. How do you set the current umask (User File Creation Mask) and return the previous value?
# The umask is a default system setting that determines the permissions assigned to newly created files and directories.
# The umask is a three-digit octal number (e.g., 022),
# where each digit subtracts permissions from the corresponding user, group, and others.
# If the umask is 022, for example, it removes write permissions for group and others from the default permissions.
prev_umask = os.umask(0)#  temporarily sets the umask to 0, which would allow all default permissions (no restrictions).
# The return value (prev_umask) stores the previous umask before it was changed.
print("Previous Umask Value:", prev_umask)
os.umask(prev_umask)  #  restores the original umask to its previous state.
# This ensures that the temporary change to the umask doesn't affect other parts of the program or subsequent processes.
print("-" * 40)
print("-" * 40)

#**********************************************************************************************************************************************#

# 7. How can you walk through a directory tree, including all subdirectories and files?

for root, dirs, files in os.walk('.'):
    print("Root Directory:", root) # root: The current directory path.
    print("Subdirectories:", dirs) # dirs: A list of the names of the subdirectories in the current directory.
    print("Files:", files) # files: A list of the names of the non-directory files in the current directory.
    print("*" * 40)
print("-" * 40)

#**********************************************************************************************************************************************#
#**********************************************************************************************************************************************#