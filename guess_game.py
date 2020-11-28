first_name=str(input('Enter your Name: '))
second_name=input("Enter Second Player Name: ")
print("          Welcome",first_name,"in guessing number game\n Enter any Number and let's see in how many guess",second_name,"can find it\n")
no=int(input())
print('Hi',first_name,'Your number is',no,'press enter for clear screen so',second_name,'can not see your number')
cls = lambda: print('\n'*100)
cls()
print("           welcome",second_name,"Enter any number and let's see in how many guess you can find entered number by",first_name)
user_input=int(input())
i=1
while(1):
    if(no==user_input):
        print('Congress',second_name,'!! you have found, Number is',user_input,'\ntotal guess',i,'\n')
        break
    elif(user_input<no):
        user_input=int(input('Enter grater Number'))
    elif(user_input>no):
        user_input=int(input('Enter less Number'))
    i=i+1
        
    
