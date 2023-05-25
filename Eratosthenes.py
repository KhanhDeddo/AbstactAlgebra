#Thuat toan sang Eratosthenes.
import os
from IPython.display import clear_output

def Eratosthenes(n):
    lis=[]
    for i in range(2,n+1):
        lis.append(i)
    for start in lis:
        count=0
        for n in lis:
            if n%start==0:
                count+=1
                if count>1:
                    lis.remove(n)
    return lis

def Control():
    while True:
        os.system("cls")
        clear_output()
        print("Thuat toan sang Eratosthenes.")
        n=int(input("Nhap mot so tu nhien bat ki: "))
        print("\nDanh sach so nguyen to.")
        print(Eratosthenes(n))
        print("\nDong chuong trinh nhap:-1")
        control=input("Tiep tuc an Enter.")
        if control=="-1":     
            os.system("cls")
            clear_output()
            print("Chuong trinh da dong.")
            break
Control()
