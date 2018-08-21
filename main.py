lecture_dict = dict()                    
prof_dict = dict()

for i in range(0, int(input())):                                #Getting input
    prof = input()
    subs = [x.strip() for x in input().split(',')]
    prof_dict[prof] = subs
for i in range(0, int(input())):
    section = input()
    lecture = [x.strip() for x in input().split(',')]
    lecture_dict[section] = lecture
    
def method(dicts, value):                                        #Getting professor name from subject 
    for k, v in dicts.items():
        for i in v:
            if i == value:
                return k

for x, y in lecture_dict.items():                                
    print(str(x) + ": ", end="")
    for i in range(0, 2):
        print(str(method(prof_dict, y[i])), end="")             
        if(i == 0):                                               #To Make it look pretty
            print(", ", end="")
        else:
            print()


'''Sample Input
3
Prof. Arjun
Data Structures, Digital Electronics, Artificial Intelligence
Prof. Reema Bhatnagar
C Programming, Financial Accounts 
Prof. Govind Rangaraja
Discrete Mathematics, Information Theory
3
BCA-2A
C Programming, Discrete Mathematics 
MCA- 3A
Data Structures, Information Theory 
MCA-5A
Artificial Intelligence, Discrete Mathematics


Sample Output
MCA- 3A: Prof. Arjun, Prof. Govind Rangaraja
BCA-2A: Prof. Reema Bhatnagar, Prof. Govind Rangaraja
MCA-5A: Prof. Arjun, Prof. Govind Rangaraja
'''
