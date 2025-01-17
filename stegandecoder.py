from PIL import Image
import numpy as np
import os
import sys

def stegdecode():
    
    colors = {
    'error':'\033[31;1m[x] ',
    'msg':'\033[36;1m ',
    'success':'\033[33;1m ',
    'white':'\033[37;1m '
    }
    
    imagepath=input(colors['white'] + "Enter image path: ")
    if os.path.exists(imagepath):
        image = Image.open(imagepath)
    else:
        print(colors['error'] + 'File path invalid xD')
        sys.exit()


    extracted= ''

    i=0
    img=np.array(image)
    for x in range(73):
        r,g,b = img[x,0]
        pixel=r,g,b
        
        if i<216:
            rbit=bin(r)
            rlbit=rbit[-1]
            extracted+=str(rlbit)   

        if i<216:
            gbit=bin(g)
            glbit=gbit[-1]
            extracted+=str(glbit)    

        if i<216:
            bbit=bin(b)
            blbit=bbit[-1]
            extracted+=str(blbit)    


    chars = []
    for i in range(len(extracted)//8):
        byte = extracted[i*8:(i+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    print('\n' + colors['success'] + ''.join(chars[2:-2]))
