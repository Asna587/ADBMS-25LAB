file="file4.txt"
with open(file,'r') as source:
      f1=source.read()
      content=f1.upper()
with open(file,'w')as source:
      source.write(content)
print(f"content of file (file) is capitalized")
      
