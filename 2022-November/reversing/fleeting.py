"""
Description:
- 😉

Attachments:
- print((f:=lambda s:s and[s[0]^s[-1],*f(s[::-1][1:])])([*open("flag",'rb')][0]))
- #[20, 37, 47, 47, 56, 52, 38, 46, 51, 56, 23, 58, 57, 50, 86, 95, 95, 103, 0]
"""

print((f := lambda s: s and [s[0] ^ s[-1], *
                             f(s[::-1][1:])])([*open("flag", 'rb')][0]))


input = [20, 37, 47, 47, 56, 52, 38, 46, 51,
         56, 23, 58, 57, 50, 86, 95, 95, 103, 0]

print((f := lambda s: s and [s[0] ^ s[-1], *
                             f(s[::-1][1:])])(input))


print([*open('flag', 'rb')][0])
