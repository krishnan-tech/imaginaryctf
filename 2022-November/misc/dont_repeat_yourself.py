"""
Description:
- There's many software design principles you should follow in order to write clean code. In this challenge, please make sure you DRY, thank you and good luck!

Attachments:
- nc puzzler7.imaginaryctf.org 7001 
- https://imaginaryctf.org/f/XLoOK#dry.py
"""

"""
Solution - eval(input())
"""

while True:
    inp = input('>>> ')
    check = 0
    used = set()
    for c in inp:
        check ^= ord(c)
        if c in used:
            print("DRY!")
            exit()
        used |= {c}
    if check:
        print("Non-zero checksum!")
        exit()
    exec(inp)
