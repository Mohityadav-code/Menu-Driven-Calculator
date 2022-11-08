n=input("Enter a word and i will check whether the word is panidrome :")
lastLetter=len(n)-1
flag=0


for i in range(lastLetter):

    if n[lastLetter-1]!=n[i]:
        flag=1
        
        break
if flag==1:
    
    for j in range(lastLetter,-1,-1):

        if n[i]==n[j]:

            print("Yes it palnidrome")
            break
        elif n[i]!=n[j]:

            print("No it is not palindrome")   
            break
        else:
            print("No it is not palindrome") 
