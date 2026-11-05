from PIL import Image
import math

def decoder(key):
    len = lenget()
    codeW = int(math.sqrt(len))+1
    charl = []
    flag = False
    for j in range(1 , ((codeW-1)*10)+2 , 10):
        
        if flag == True : 
            break
        for i in range(1 , ((codeW-1)*10)+2 , 10):
            
            pxcount = (((j//10)+1)-1)*codeW+((i//10)+1)

            if pxcount > len:  
                flag = True
                continue
            
            r , g , b ,a = img.getpixel((i , j))
            uni = (r*key) + g
            char = chr(uni)
            charl.append(char)
    code = "".join(charl)
    return code
        

def lenget():
    r , g , b ,a = img.getpixel((100,100))
    len = (r*256) + g
    return len

img = Image.open("Encoded.png")
key = int(input("What is the code? "))
try:
    print(decoder(key))
except: 
    print("wrong code!")