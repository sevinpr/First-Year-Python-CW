# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. # Any code taken from other sources is referenced within my code solution.
# Student ID: w18993222
# Date: 18/04/2022
from itertools import zip_longest
tuple=('')
progress_data=[]
Proceed = 'y'
Progress = Trailer = Retriever = Exclude = ''
def Validation (x):
    Range = [120, 100, 80, 60, 40, 20, 0]
    if x not in Range:
       print('Out of range.\n')
    else:
       return True
print('Staff version with Histogram\n')
while Proceed=='y':
    while True:
        try:
            print('')
            Credit_Pass=int(input('Enter your total Pass credits : '))
            if Validation(Credit_Pass)!=True:
                continue
            else:
                break
        except ValueError:
            print('Integer required.\n')
            continue
    while True:
        try:
            Credit_Defer=int(input('Enter your total Defer credits : '))
            if Validation(Credit_Defer)!=True:
                continue
            else:
                break
        except ValueError:
            print('Integer required.\n')
            continue
    while True:
        try:
            Credit_Fail=int(input('Enter your total Fail credits : '))
            if Validation(Credit_Fail)!=True:
                continue
            else:
                break
        except ValueError:
            print('Integer required.\n')
            continue
    total_credits=Credit_Pass+Credit_Defer+Credit_Fail
    if total_credits!=120:
        print('Total Incorrect.\n')
    elif Credit_Pass==120:
        Progress+='*'
        print('Progress\n')
        tuple=(Credit_Pass,Credit_Defer,Credit_Fail)            
        progress_data.append("Progress - %s\n"%str(tuple)[1:-1])   #converting tuple to string because tuple immutable and cannot be appended to a list
    elif Credit_Pass==100:
        Trailer+='*'
        print('Progress (module trailer)\n')
        tuple=(Credit_Pass,Credit_Defer,Credit_Fail)
        progress_data.append("Progress (module trailer) - %s\n"%str(tuple)[1:-1])   #https://stackoverflow.com/a/43089203 https://docs.python.org/3/library/stdtypes.html#old-string-formatting
    elif Credit_Fail>=80:
        Exclude+='*'
        print('Exclude\n')
        tuple= (Credit_Pass,Credit_Defer,Credit_Fail)
        progress_data.append("Exclude - %s\n"%str(tuple)[1:-1])
    else:
        print('Module retriever\n')
        Retriever+='*'
        tuple=(Credit_Pass,Credit_Defer,Credit_Fail)
        progress_data.append("Module retriever - %s\n"%str(tuple)[1:-1])
    while True:
        Proceed=input('Would you like to enter another set of progress_data?\n' "Enter 'y' for Yes or 'q' to Quit and view results : ").lower()
        if Proceed!='y' and Proceed!='q':
            continue
        else:
            break
print('')
print('-'*65)
print('Horizontal Histogram\n')
print('Progress',len(Progress),'  : ', Progress,'\n''Trailer',len (Trailer),'   : ',Trailer,'\n''Retreiver',len(Retriever),' : ',Retriever,'\n''Exclude',len(Exclude),'    : ',Exclude)
print('')
print(len(Progress+Trailer+Retriever+Exclude), 'outcomes in total.')
print('-'*65)
print('')
print('Vertical Historgram\n')
print(' Progress ',len(Progress),'| Trailer',len(Trailer),'| Retriever',len(Retriever),'| Exclude',len(Exclude))
for a,b,c,d in zip_longest(Progress,Trailer,Retriever,Exclude,fillvalue=' '):   #https://stackoverflow.com/a/55573972   https://docs.python.org/3/library/itertools.html#itertools.zip_longest
    print(' '*3,a,' '*11,b,' '*10,c,' '*10,d)
print(len(Progress+Trailer+Retriever+Exclude), 'outcomes in total.\n')
f=open("cw.txt",'w')
f.write(''.join(progress_data))
f.close()
f=open("cw.txt",'r')
print(f.read())