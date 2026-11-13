from PIL import Image
import math

def decoder(key):

    len = lenget()
    codeW = int(math.sqrt(len))+1
    char_list = []
    flag = False
    
    for j in range(1 , ((codeW-1)*10)+2 , 10):

        # this statement is to avoid the error of index out of range when the code is less than the total number of pixels in the imaginary cube
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
            char_list.append(char)
    code = "".join(char_list)
    return code

# find the length of the code in the image at pixel (100,100)
def lenget():
    r , g , b ,a = img.getpixel((100,100))
    len = (r*256) + g
    return len

#for local testing of the decoder function
if __name__ == "__main__":   

    while  True:
        try:
            imgl = input("Enter your images directory... \n")
            img = Image.open(imgl).convert("RGBA")
            break
        except:
            print("Image not found!")

    while True:
        try:
            key = int(input("Enter your key: "))
            if key <= 0:
                print("Wrong key!")
                continue
            else:
                break
        except ValueError:
            print("Wrong key!")
            exit()
        
    print(decoder(key))