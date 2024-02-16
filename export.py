import glob, os, json, sys
try:
    path = sys.argv[1]
    if not os.path.isdir(path): raise
except:
    print("Invalid syntax. Use \"export <path>\" to export all contents from folder <path> to <path>\\data.rawexp.")
    exit()
print("Exporting...")
res = {}
for filename in glob.iglob(f'{path}\\**', recursive=True):
    if os.path.isfile(filename): # filter dirs
        file = filename[len(path + "\\"):]
        data = open(filename, "rb")
        res[file] = data.read().decode("latin1")
        data.close()
data = open(path + "\\data.rawexp", "w")
json.dump(res, data)
data.close()