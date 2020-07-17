
#Schreiben Sie ein Programm, 
#das alle durch 3 und 7 teilbaren Zahlen zwischen j und k (k > j) ermittelt.

j=int(input("Please select min:"))
k=int(input("Please select max:"))


def finder (j,k):
    while j<=k:
        if j%3==0 and j%7==0 :
            j+=1
        else:
            j+=1   
    return (j,k)
print("Results:",finder(j,k))