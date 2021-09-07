def rep(x,y):

    with open('sample.txt', 'r', encoding ="utf-8") as file : # reading the file
        filedata = file.read()
    
    filedata = filedata.replace(x,y) #replacing string

    with open('sample-new.txt', 'w', encoding = "utf-8") as file: #write again
        file.write(filedata)


while True:
    wtr = str(input("Write the string you want to replace: "))
    rpmnt = str(input("Write the raplacement string: "))
    rep(wtr,rpmnt)
