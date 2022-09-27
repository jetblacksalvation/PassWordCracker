password = input("give me the password")
#iterate through first index once finished iterating thorugh first, iterate second and repeat until length of password -1 is reached     
newlist =[int(x)for x in password]
print(newlist)#new list is what you check index_list to 
#if new list == index list - found match!
vec_int = [0 for x in range (len(password))]#creates a vector of ints equal to the size of f_list, holds index values 

for x in range(len(password)**9):
    
    
    if vec_int == newlist:
        print(vec_int, " is password")
        #exit()
    elif vec_int != newlist:
        print(vec_int)
        vec_int[0]+=1
        if vec_int[0] >= 9:
            vec_int[0] = 0
            vec_int[1]+=1
            for elem, y in enumerate( vec_int):
                if elem >=9:
                    vec_int[y+1]+=1
