import os, json, sys
cwd = os.getcwd()
try:
    path = sys.argv[1]
    if not os.path.isfile(path) or path.endswith(".rawexp"):
        raise
except:
    print("Invalid file. Use \"import <file>\" to import contents of <file> to the current dir.")
    exit()
print("Importing...")
data = open(path, "rb")
file = dict(json.load(data))
for i, j in file.items():
    full_path = cwd + "\\" + i
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    file_ = open(full_path, "wb")
    file_.write(j.encode("latin1"))
    file_.close()