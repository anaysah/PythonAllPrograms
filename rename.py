import os
import re

def main():
   
    folder = os.getcwd()
    for r in os.listdir():
        src = folder +"\\" + r
        dst =re.findall("(.*)\.txt",r)
        if dst!=[]:
            os.rename(src,dst[0]+".c")
 
if __name__ == '__main__':
    main()
