while True :
    print("choose your option:\n\t1)Encrypt"
          "\n\t2)decrypt"
          "\n\t3)Exit")
    choice=int(input("your choice:"))
    if choice == 1:
        plane_text=input("Enter you Text")
        encrypt_text=""
        for c in plane_text:
            x=ord(c)*2+5
            encrypt_text+=chr(x)
        print("encrypted text is:", encrypt_text)
    elif choice == 2:
        encrypt_text=input("enter your decrepted text:")
        plane_text=""
        for c in encrypt_text:
            x=(ord(c)-5)//2
            plane_text+= chr(x)
        print("text is:",plane_text)
    else:
        print("You select Exit")
    break