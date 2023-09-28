import os

# Do the following task using the os module
#1. create a folder and name the folder 'os_exercises.'                                                  
#2. In that folder create a file. Name the file 'exercise.py'                                                                            
#3. get input from the console and write it to the file.                                                 
#   * In VSCode and using Notebooks the console will pop up in the top of the editor. So ```input()``` will propt the user for input, and i VScode this is in the top of the editor. 
#4. repeat step 2 and 3 (name the file something else).                                                  
#5. read the content of the files and and print it to the console.

#3
os.chdir("ses4/os_exercises")
folder = input("Write foldername: ")
os.mkdir(folder)
os.chdir(folder)
filename = input("Write filename: ") + ".py"

file = open(filename, "w")
file.write(input("Write file content: "))

file.close()

os.system('python ' + filename)

os.remove(filename)

os.chdir('..')

os.rmdir(folder)


