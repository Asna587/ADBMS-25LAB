file="file1.txt"
w1='write'
w2='replaced'
with open(file,'r') as source:
    f1=source.read()
    content=f1.replace(w1,w2)
with open(file,'w') as source:
    source.write(content)
print(f"content of file {file} is replaced")
