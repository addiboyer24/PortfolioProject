import sys

def pack_objcode(string):
    for x in range(0, len(string), 2):
        print(chr(int("0x" + string[x:x+2], 16)), end='')


def main(argv):
    if(len(argv)!=1):
        print("Usage <String to pack>")
    else:
        pack_objcode(argv[0])
        print()
        
if(__name__ == '__main__'):
    main(sys.argv[1:])
