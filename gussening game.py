x=56
print("WELCOME TO THE NO. GUSSENING GAME\nHOW MANY GUSSES YOU NEED")
j=int(input())
while(True):
    if j==0:
        print("YOU HAVE RUN OUT OF GUSSES")
        break
    print("ENTER YOUR NO.")
    i = int(input())
    if i>x:
        print("ENTERED NO. IS HIGHER")
        j=j-1
        print("NO. OF GUSSES LEFT",j)
        continue
    if i<x:
        print("ENTERED NO. IS LOWER")
        j=j-1
        print("no. of gusses left",j)
        continue
    else:
        print("CONGRATS YOU HAVE GUSSES THE NO. CORRECTLY",i)
        break