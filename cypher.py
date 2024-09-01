import logo as l
print(l.logo) 
print("Welcome to caesar's cipher")
def encrypt(msg,shift):
    e_msg=""
    for i in msg:
        a_check=i
        if a_check not in l.alphabets:
            l.alphabets+=a_check
        e_ind=(l.alphabets.index(a_check)+shift)%len(l.alphabets)
        e_msg+=l.alphabets[e_ind]
    print(e_msg)

def decrypt(msg,shift):
    e_msg=""
    for i in msg:
        a_check=i
        if a_check not in l.alphabets:
            l.alphabets+=a_check
        e_ind=(l.alphabets.index(a_check)-shift)%len(l.alphabets)
        e_msg+=l.alphabets[e_ind]
    print(e_msg)

esc=""
while esc!="yes":
    ch=input("Do you want to encode or decode a message?\n").lower()
    if ch=="encode":
        msg=input("Type your message\n").lower()
        shift=int(input("Type the shift number\n"))
        encrypt(msg,shift)
    elif ch=="decode":
        msg=input("Type your message\n").lower()
        shift=int(input("Type the shift number\n"))
        decrypt(msg,shift)
    else:
        print("Please enter correctly!")
        continue
    esc=input("Do you want to quit this program?\n").lower()

print("Thank You for using caesar's cipher!!!!")