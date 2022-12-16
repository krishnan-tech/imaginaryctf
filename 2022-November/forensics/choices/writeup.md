```
Description:
- You'll look up and down streets. Look 'em over with care. About some you will say, "I don't choose to go there." With your head full of brains and your shoes full of feet, you're too smart to go down any not-so-good street.

Attachments:
- https://imaginaryctf.org/f/u76Tz#flag.zip
```

Download the file using this command (Size: 33MB): `curl "https://s1.fdow.nl/u76Tz-flag.zip" -o "flag.zip"`

```
After downloading the file, I started unzipping the file, then I realize that, it is a loop or something, and doing so will not help.

Then I thought of using grep command to search text. After some digging I found the flag -a or --text to search binaries.
```

```
man page of grep

File and Directory Selection
       -a, --text
              Process a binary file as if it were text; this is equivalent to the --binary-files=text option.
```

Solution:
`grep --text ictf flag.zip` or `grep -a ictf flag.zip`

Flag:
`ictf{th3re_are_po1nts_to_b3_scored._ther3_are_gam3s_to_be_won.}`
