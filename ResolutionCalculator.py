def rescal(q):
    pd = ((((q[0])**2)+((q[1])**2))**(0.5)) # diagonal in pixels
    ppi = ( pd / (q[2]) ) # ppi
    real = ( ppi * (100/q[3]) ) # s is scaling

    print(f"Pixel Diagonal: {pd:.3f}, PPI: {ppi:.3f} , After Scaling: {real:.3f}")

    return pd , ppi , real

while True:
    inn = str(input("Write your width, hight, screen size(inch) and scaling by seperating with commas: "))
    innn = (inn.split(","))
    innnn = list() 
    for i in innn:
        i = float(i)
        innnn.append(i)
    print(innnn)
    rescal(innnn)
