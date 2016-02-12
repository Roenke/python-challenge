#!/usr/bin/env python3
import re
string = """big string from page sourse"""

print(''.join(re.findall('[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}',string))) # linkedlist