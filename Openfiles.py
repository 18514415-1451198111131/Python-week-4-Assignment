#reading the file and printing it's contents
try:
    #reading existing file
    filename = input("BM.txt:")
    with open(BM.txt, "r") as file:
        content = file.read()
        print(content) 
#creating and writing a new file
    GOMD = input("BM.txt:")
    new_content = input("GOMD.txt:")
    with open(GOMD, 'w') as file:
        mod_file = content + '\n' + new_content
        file.write(mod_file)
    print(f"created successfully {mod_file}")
except FileNotFoundError: 
    print("file not found/error")
