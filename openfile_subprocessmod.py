import subprocess    

path_to_notepad = "C:\\Windows\\system32\\notepad.exe"
path_to_file = r"C:\Users\AjaySahu\Desktop\stl.txt"


subprocess.call([path_to_notepad, path_to_file])
