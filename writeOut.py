file = open("newfile.txt", "w")
x = 2 
while x <=20:
    print x
    x +=2
if x==4:
    file.write("x is 4.")
else:
    file.write("x is not 4.")
file.close()
