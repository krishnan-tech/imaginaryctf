"""
Description:
- I'm not happy with how one of the regex challenges last month landed, which means more regrets for everybody!

Attachments:
- nc puzzler7.imaginaryctf.org 7000 
- https://imaginaryctf.org/f/wcwlI#server.py
"""

"""
Solution - Main idea here is to use ".*" in regex!!
Flag - ictf{short_flag_5ddc}
"""


from pwn import *
p = remote("puzzler7.imaginaryctf.org", 7000)

flag = "ictf{"

while "}" not in flag:
    for c in "abcdefghijklmnopqrstuvwxyz_}0123456789":
        rx = flag + c + ".*"
        p.recvuntil(":")
        p.sendline(rx)
        print(rx)
        if b"Match!" in p.recvline():
            flag += c
            break
print(flag)
