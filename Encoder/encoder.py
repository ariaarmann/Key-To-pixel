from PIL import Image
import math
def encoder(code ,clen , key , img):
    lenset(clen , img)
    codeW = int(math.sqrt(clen))+1
    flag = False
    for j in range(1 , ((codeW-1)*10)+2 , 10):
        
        if flag == True:
            break

        for i in range(1 , ((codeW-1)*10)+2 , 10):

            #(((j//10)+1)-1) to declare that there is (((j//10)+1)-1) rows before the current row
            # above rows should be multiplied by codeW to get the total number of pixels in the above rows
            # ((i//10)+1) to show the current pixel in the current row
            pxcount = ((( j // 10 ) + 1 ) - 1 ) * codeW + ((i // 10 ) + 1 )

            #this statement is to avoid the error of index out of range when the code is less than the total number of pixels in the image
            if pxcount > clen:
                flag = True
                continue
            
            r , g , b ,a = img.getpixel((i , j))

            # -1 to convert to 0-based index
            ennum = ord(code[pxcount-1])

            #ZeroDivisionError is avoided by using the if statement to check if the key is greater than 0
            r = ennum //key
            g = ennum %key

            img.putpixel((i , j) , (r , g , b , a))

# this function is to set the length of the code in the image at pixel (100,100) so that it can be retrieved later when decoding
def lenset(clen , img):
    r , g , b ,a = img.getpixel((100,100))
    r = clen // 256
    g = clen % 256
    img.putpixel((100,100) , (r ,g , b , a))

#for local testing of the encoder function
if __name__ == "__main__":

    while  True:
        try:
            imgl = input("Enter your images directory... \n")
            img = Image.open(imgl).convert("RGBA")
            break
        except:
            print("Image not found!")
    

    code = input("input your code: ")

    while True:
        try:
            key = int(input("Enter your key (key>0): "))
        except ValueError:
            print("KEY SHOULD BE AN INTEGER")
            
        #ZeroDivisionError is avoided by using the while loop to check if the key is greater than 0
        else:
            if key <= 0:
                print("KEY VALUE SHOULD BE ABOVE ZERO!!")
                continue
            else:
                break



    clen = len(code)
    encoder(code , clen , key , img)
    try:
        img.save("Encoded.png")
    except:
        print("An error occurred while saving the image. Please make sure the file is not open in another program and you have write permissions.")
