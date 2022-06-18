def getUp(mail):

    up = ""

    for i in mail:
        if i == 'u' or i == 'p':
            continue

        elif i == '@':
            break
        
        up = up + i

    print(up)

getUp("up201904996@fe.up.pt")
#