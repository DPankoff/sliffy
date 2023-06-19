# this file get signature func with python

import sys
import re


class Parser:
    
    def __init__(self):
        print(self)
    
    def parse_c_function_signature(self,signature):
        pattern = r"(\w+)\s+(\w+(?:\.\w+)*)\s*\((.*?)\)"
        match = re.match(pattern, signature)

        if match:
            return_type = match.group(1)
            function_name = match.group(2)
            args = match.group(3).split(',') if match.group(3) else []
            args = [arg.strip().partition(" ")[0] for arg in args]
            return function_name, return_type, args
        else:
            raise ValueError("Invalid function signature")





