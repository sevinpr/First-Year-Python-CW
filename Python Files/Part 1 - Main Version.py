# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. # Any code taken from other sources is referenced within my code solution.
# Student ID: w18993222
# Date: 18/04/2022
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
    elif Credit_Pass==100:
        Trailer+='*'
        print('Progress (module trailer)\n')
    elif Credit_Fail>=80:
        Exclude+='*'
        print('Exclude\n')
    else:
        print('Module retriever\n')
        Retriever+='*'
    while True:
        Proceed=input('Would you like to enter another set of data?\n' "Enter 'y' for Yes or 'q' to Quit and view results : ").lower()
        if Proceed!='y' and Proceed!='q':
            continue
        else:
            break
print('')
print('-'*65)
print('Horizontal Histogram\n')
print('Progress',len(Progress),'  : ', Progress,'\n''Trailer',len (Trailer),'   : ',Trailer,'\n''Retreiver',len(Retriever),' : ',Retriever,'\n''Exlude',len(Exclude),'    : ',Exclude)
print('')
print(len(Progress+Trailer+Retriever+Exclude), 'outcomes in total.')
print('-'*65)