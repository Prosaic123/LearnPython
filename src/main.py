file_path = "data/test.txt"

file = open(file_path,"r", encoding="utf-8")

while True:
    line = file.readline()
    
    print(line.strip())
    
    if not line:
        break

file.close()