# JACS
Just Another Caesar Sala... I mean cipher. Simple plain-text symmetric key encryption/decryption with a password(key) strength checker(ie password requirements) written in python.


I'm new to writing code and this is my first creation. Let me know if there are issues or if you have some betterment ideas.

PROCESS:

The cipher converts a password (checked for \**minimum requirements*) into a numeric key using the ascii chart and removes all zeroes. The encryption/decrytion encodes/decodes the message with the key by moving left/right whether the number(two digits) is odd/even in the \*\**alphabet*. Commented out is an option to add 2 characters per character to the encryption(Must include the commented out portion in the decrypt if doing this(elines 57/58 and 61/62, dlines 70/71)). That's the gist of it.

UTILIZE:

To use via the command line:
  - ./jacs.py [file] [password] [encrypt or decrypt(e/d)]  -- will print to the terminal (recommend [ > [new_file_name]] to output straight to a file).
    - Encrypt/Decrypt coloring is commented out to prevent error in case content is not directly output to a file. If always directly input/output from/to a file then you can uncomment that line(s) and comment out the subsequent line(s) (colorlines (e)97/98 and (d)100/101, 102/103)

To use in a script import jacs and use encrypt() or decrypt() and it'll sort out the rest.


\**minimum requirements* for the password: 1 uppercase, 1 lowercase, 1 number, 1 symbol, 12 characters minimum, no more than 2 identical or 2 sequential characters(case insensitive) in sequence.

\*\**alphabet* can be redeclared by moving around the characters in it further complicating the cipher(another alphabet(alfa line 5) included demonstrating what I mean). The alphabet you use must contain all the characters in the original or else it will cause an error.



KNOWN ISSUES:

  - It's possible for different(incorrect) keys to partially decrypt the same encrypted message but likelihood is reduced with stronger passwords. Unlike a standard Caesar cipher where you only have to get it right once; this cipher increases the difficulty by increasing and varying the individual characters conversion key length and shift.
  - The password checker uses the decimal order of the ascii chart to determine sequential characters. For example "\`aB" or "{zy" or vice versa will return an error for characters in sequence and ask for you to try another password.
