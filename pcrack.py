import PyPDF2
import sys
print('please enter PDF file name')
file1=str(raw_input())
pdf = PyPDF2.PdfFileReader(open(file1,'rb'))
print('please enter password dictionary file name')
file2=str(raw_input())
print('checking password...please wait')
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
