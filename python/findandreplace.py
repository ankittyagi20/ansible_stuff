with fileinput.FileInput(<filename>, inplace=True) as file:
  for line in file:
  print(line.replace("search_substring","replace_with"), end='') #end is required to stop adding extra newline, end is bydefault newline


# Read in the file
with open('file.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('ram', 'abcd')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)
