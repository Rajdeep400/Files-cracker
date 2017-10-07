import xlrd
import sys
print("enter the name of a excel_file......")
file1=str(raw_input())
wordbook=xlrd.open_wordbook('file1','rb')
print("please enter the pasword dictionary file name")
file2=str(raw_input())
print("checking password.......... please wait........")
f=open(file2,'r+')
str=f.read().splitlines()
n=len(str)
for line in range(0,n):
    print(str[line])
    p=pdf.decrypt(str[line])
    if p>0:
        print 'password found: ',str[line]
        f.close()
        sys.exit()
print 'password not found'
f.close()
