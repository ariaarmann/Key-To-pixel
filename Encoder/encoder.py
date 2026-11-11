from PIL import Image
import math
def encoder(code ,clen , key):
    lenset(clen)
    codeW = int(math.sqrt(clen))+1
    flag = False
    for j in range(1 , ((codeW-1)*10)+2 , 10):
        
        if flag == True:
            break
        for i in range(1 , ((codeW-1)*10)+2 , 10):
            
            pxcount = (((j//10)+1)-1)*codeW+((i//10)+1)

            if pxcount > clen:
                flag = True
                continue
            
            r , g , b ,a = img.getpixel((i , j))
            ennum = ord(code[pxcount-1])
            r = ennum //key
            g = ennum %key
            img.putpixel((i , j) , (r,g,b , a))


def lenset(clen):
    r , g , b ,a = img.getpixel((100,100))
    r = clen // 256
    g = clen % 256
    img.putpixel((100,100) , (r ,g , b , a))
    

imgl = input("ENter your images directory... \n")
img = Image.open(imgl).convert("RGBA")
code = input("input your code: ")
key = int(input("Enter your key (key>0): "))

while key <= 0 :
    print("KEY VALUE SHOULD BE ABOVE ZERO!!")
    key = int(input("Enter your key (key>0): "))

clen = len(code)
encoder(code , clen , key)

img.save("Encoded.png")

