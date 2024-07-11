def comp_chances(n1,n2,n3):
    count=0
    while(True):
        no = int((n1 + n2) / 2)
        count+=1
        if(no>n3):
            n2=no
        elif(no<n3):
            n1=no
        else:
            break
    return count

