def tann(x,y):
    h = (((x**2)+ (y**2)) ** (0.5))
    sinn = y / h
    coss = x / h
    tann = sinn / coss
    print(f"Sin: {sinn:.3f} , Cos: {coss:.3f} , Tan : {tann:.3f} , Hipotenüs: {h:.3f}")
    return h , sinn , coss , tann

print(tann(1,1))