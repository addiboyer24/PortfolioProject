import sys

def string_to_hex(string):
    ret = ''
    for char in string:
        ret = hex(ord(char))[2:] + ret
    
    return '0x'+ret
    

def main(argv):

    if(len(argv) != 1):
        print("Usage string_to_hex.py <string to convert>")
    else:
        print(string_to_hex(argv[0]))

if(__name__ == '__main__'):
    main(sys.argv[1:])
