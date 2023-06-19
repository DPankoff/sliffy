# this file get signature func with python
import  r2pipe
import sys
import re

from parser import Parser
from config import *

r = r2pipe.open(app_name)

# get all info with radare
print(r.cmd('aaaa'))

# get list function for analyze
print(r.cmd('afl'))


def func(address):
    print(r.cmd('s  ' + address))

    sign = r.cmd('afcf')
    print(sign)

    p = Parser()
    function_name, return_type, args = p.parse_c_function_signature(sign)
    
    print("Function Name:", function_name)
    print("Return Type:", return_type)
    print("Arguments:", args)

 
adr = input("Get addres for find signature: ")

print(adr)

func(adr)



