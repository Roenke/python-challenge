#!/usr/bin/env python3
string = """map"""
offset = ord('m') - ord('k')
result = []
for ch in string:
    if ch in ' ,.()\'/':
        result.append(ch)
    elif ch in 'yz':
        new_ch = 'a' if ch == 'y' else 'b' 
        result.append(new_ch)
    else:
        result.append(chr(ord(ch) + offset))

print(''.join(result))
