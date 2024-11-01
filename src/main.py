file_path = "data/test.txt"

file = open(file_path,"r", encoding="utf-8")

file_name = file.name

print("文件名字："+ file_name)

while True:
    line = file.readline()
    
    print(line.strip())
    
    if not line:
        break

file.close()