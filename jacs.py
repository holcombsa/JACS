#! /usr/bin/env python3

import sys

# alfa = "Z.Cak" + chr(34) + "BY_4AuXb)5Wlv,V6-cUm7]Tw|" + chr(10) + "dS8(nRx':9/QeoP!yO" + chr(32) + "f@Np<zM#g+Lq{$K0;hJ%rI>1}^Hi" + chr(92) + "sG=&2Fj*Et[3D?"
alfa = "qwertyuiopasdfghjklzxcvbnm" + chr(34) + "0123456789" + chr(92) + "~`!@#$%^&*()_+-=[]{}|':;<>?/.," + chr(10) + "QWERTYUIOPASDFGHJKLZXCVBNM" + chr(32)
alfa_plus = alfa * 3



def char_err(char):
  return color(f"Character not recogized: {char}", "red")



def pw_error(pwe):
  incompatible_password = "Your password must contain a minimum of:\n1 uppercase letter\n1 lowercase letter\n1 number\n1 symbol\n12 characters\nno more than 2 identical characters in succession\nno more than 2 sequential characters"
  return input(color(f"{incompatible_password}\n>> {pwe} <<", "red") + "\nTry another password ")



def pw_check(pw):
  up, lo, nu, sy, char_cnt = 0,0,0,0,0
  for char in pw:
    if char not in alfa:
      print(char_err(char))
      return pw_check(pw_error(pw))
    if char_cnt != 0:
      if char_cnt != len(pw)-1:
        previous_char, next_char, char_lo = pw[char_cnt-1].lower(), pw[char_cnt+1].lower(), char.lower()
        if previous_char == char_lo and next_char == char_lo: # 111aaa
          print(color(">> Identical characters in sequence <<", "red"))
          return pw_check(pw_error(pw))
        elif ord(previous_char)-1 == ord(char_lo) and ord(next_char)+1 == ord(char_lo): #321cba
          print(color(">> Sequential characters <<", "red"))
          return pw_check(pw_error(pw))
        elif ord(previous_char)+1 == ord(char_lo) and ord(next_char)-1 == ord(char_lo): #123abc
          print(color(">> Sequential characters <<", "red"))
          return pw_check(pw_error(pw))
    char_cnt +=1
    if char.isupper(): up += 1
    elif char.islower(): lo += 1
    elif char.isdigit(): nu += 1
    else: sy += 1
  if up and lo and nu and sy >= 1 and len(pw) >= 12: pass
  else: 
    print(color(">> Missing required characters <<", "red"))
    return pw_check(pw_error(pw))
  return gen_pkey(pw)


  
def gen_pkey(pw_true):
  print("... standby ...")
  pkey_ls = [ord(i) for i in pw_true]
  pkey_temp = 1
  for n in pkey_ls[::5]: pkey_temp += n*n
  for n in pkey_ls[::3]: pkey_temp -= n
  for n in pkey_ls[::2]: pkey_temp += n
  pkey = pkey_temp ** pkey_temp
  if str(000) in str(pkey):
    pkey = str(pkey).replace("000","")
  return str(pkey)



def encrypt(msg, passwd):
  passkey, emsg, i = pw_check(passwd), "", 0
  for char in msg:
    num_key, two_digs = int(passkey[i]), int(passkey[i:i+2])
    if char not in alfa: return char_err(char)
    if i >= len(passkey)-1: i = 0
    if num_key % 2 == 0:
      emsg += alfa_plus[alfa.index(char)+two_digs]
#       emsg += alfa_plus[alfa.index(char)+two_digs] + alfa_plus[alfa.index(char)-num_key] + choice(alfa)
      i += 1
    else:
      emsg += alfa_plus[alfa.index(char)-two_digs]
#       emsg += alfa_plus[alfa.index(char)-two_digs] + alfa_plus[alfa.index(char)+num_key] + choice(alfa)
      i += 1
  return emsg



def decrypt(emsg, passwd):
  passkey, dmsg, i = pw_check(passwd), "", 0
  for char in emsg:
#   for char in emsg[::3]:
    num_key, two_digs = int(passkey[i]), int(passkey[i:i+2])
    if char not in alfa: return char_err(char)
    if i >= len(passkey)-1: i = 0
    if num_key % 2 != 0:
      dmsg += alfa_plus[alfa.index(char)+two_digs]
      i += 1
    else:
      dmsg += alfa_plus[alfa.index(char)-two_digs]
      i += 1
  dmsg = dmsg.replace("\\n", "\n")
  return dmsg



def color(msg, color=""):
  if color.lower() == "green": return f"\033[92m{msg}\033[00m"
  elif color.lower() == "blue" : return f"\033[96m{msg}\033[00m"
  elif color.lower() == "red": return f"\033[31m{msg}\033[00m"
  else: return f"\033[00m{msg}\033[00m"


  
def reader(f):
  lines = f.read()
  if sys.argv[3].lower() == "e" or sys.argv[3].lower() == "encrypt":
    emsg = encrypt(lines, sys.argv[2])
    print(emsg)
#     print(color(emsg, "green"))
  elif sys.argv[3].lower() == "d" or sys.argv[3].lower() == "decrypt":
    dmsg = decrypt(lines[:-1:], sys.argv[2])
#     dmsg = decrypt(lines[5:-6:], sys.argv[2])
    print(dmsg)
#     print(color(dmsg, "blue"))



def file_access(file_name):
  open_file = open(file_name, "r")
  reader(open_file)
  open_file.close()



def typed():
  msg = input("Enter message: ")
  passwd = input("Enter password: ")
  crypt = input("Encrypt or decrypt? e/d ")
  if crypt.lower() == "e" or crypt.lower() == "encrypt":
    emsg = encrypt(msg.replace("\\n", chr(10)), passwd)
    return color(emsg.replace(chr(10), "\\n"), "green")
  elif crypt.lower() == "d" or crypt.lower() == "decrypt":
    dmsg = decrypt(msg.replace("\\n", chr(10)), passwd)
    return color(dmsg, "blue")
  else: again = input("Something's wrong. Try again? y/n ")
  if again.lower() == "y": return typed()


  
try: file_access(sys.argv[1])
# except: pass
except: print(typed())
finally: pass
