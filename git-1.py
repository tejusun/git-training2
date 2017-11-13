#don't use backslash since it is an escape char (\n \t)
with open('data/1kwords.en.txt') as fh:
    # content1 = fh.read()  -- we can only read the file only once
    # content2 = fh.readlines()
    content3 = fh.read().splitlines()  #we created a variable to hold the list and close the file
#read the file line by line instead of reading the entire file in one shot
# let us create a set object

engset = set()
with open('data/1kwords.en.txt') as fh:
    for line in fh:
        engset.add(line.strip())   #line.strip will strip new line character and white space; set = add not append
print(len(engset))

spset = set()
with open('data/1kwords.sp.txt', encoding='utf-8') as fh:
    for line in fh:
        spset.add(line.strip())   #line.strip will strip new line character and white space; set = add not append
print(len(spset))

grset = set()
with open('data/1kwords.gr.txt', encoding='utf-8') as fh:
    for line in fh:
        grset.add(line.strip())   #line.strip will strip new line character and white space; set = add not append
print(len(grset))

#print(type(content1))
#print(content1)
#print(type(content3))
#print(content3)