import json
import os


def convert_file(path):
    val = os.popen("java -jar owl2vowl.jar -file CSCL.owl -output C:\\Users\\panyue\\Desktop\\tool\\CSCL.json")
    t = val.readlines()
    for line in t:
        print(line)
    print(1)

if __name__ == '__main__':
    convert_file(1)