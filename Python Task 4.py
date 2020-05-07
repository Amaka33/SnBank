import random
import sys
import os
                
start = True

while start:
    print('''GTB BANK''')
    print ('Welcome')
    print ('Register:')
    print()
    name = str(input('What is your full name? ')).upper()
    username = str(input('What is your username? ')).upper()
    password = str(input('Password: '))
    email = str(input('Input email: '))
    print()
    
    
    staff = open('staff.txt','w')
    staff.write(f'Name:{name}\nUsername:{username}\n Password:{password}\n Email{email}')
    staff.close()
                    
    
        
        
        
        
    choice = int(input('(1)To login\n(2)To close app\n--> '))
    print()
    
    check1 = True
    if choice == 1:
        new_username = str(input('Please input Username: ')).upper()            
        while check1:
            if new_username == username:
                check1 = False
                break                                            
            else:
                print('Invalid Username,try again!\n')
                new_username = str(input('Please input Username: ')).upper()
                
                                                   
        new_password = str(input('Please input your password: '))
        check2 = True        
        while check2:
            if new_password == password:
                print()
                print(f'Login Successful\nWelcome {name}')
                print()
                check2 = False
                break                
                
            else:
                print('Incorrect Password,try again!\n')
                new_password = str(input('Please input your password: '))
                check2 = True
                
    
                
    else:
        sys.exit()
        

    session = open('session.txt', 'w+')                
    choices = True
    while choices:    
        user_choice = int(input('(1) to create new bank account\n(2) to check account details\n(3) to log out\n--> '))
        print()
        
        
        if user_choice == 1:
            print()
            ac_name = str(input('Please suggest an account name? ')).upper()
            ac_balance = str(input('What is your Opening Balance? '))
            ac_type = str(input('What is your preferred account type? '))
            ac_email = str(input('Input your mail address: '))
            session.write(f'user selected (1) and gave some details:\n Account Name: {ac_name}\nAccount balance: {ac_balance}\nAccount Type: {ac_type}\nAccount_Email: {ac_email}\n\n')
            session.close()    
            counts = True
            while counts:
                x = random.uniform (1,10)
                a = str(x)
                dot = (a.index('.'))
                generated_num = (a[dot+1:-5])
                count = len(generated_num)
                if count == 10:
                    counts = False
                    break
                else:
                    counts = True        
            else:
                counts = True
                        
                        
            customer =  open('customer.txt','w')
            customer.write(f'\nAccount Name: {ac_name}\nOpening Balance: {ac_balance} Naira\nAccount Type: {ac_type}\nAccount Email: {ac_email}\nAccount Number: {generated_num}\n\n') 
            customer.close()      
            customer = open('customer.txt','r')
            print(customer.read())
            choices = True           
            print()
            
            with open('customer.txt') as f:
                with open('session.txt', 'a+') as f1:
                    for line in f:
                        f1.write (line)
                        session.close()
            
            
        elif user_choice == 2:
            print()
            acct_check = True
            while acct_check:
                acct = (input('What is your account number? '))    
                if acct == generated_num:
                    customer = open('customer.txt','r')
                    print(f'\nHere are your detail:\n{customer.read()}')           
                    acct_check = False
                    break
                else:
                    print('Please input correct account number')
                    acct_check = True
            else:
                acct_check = True
                break
                    
            choices = True
            print()
            with open('customer.txt') as s:
                with open('session.txt', 'a+') as s1:
                    for line in s:
                        s1.write (line)
                        session.close()       
                    
        elif user_choice == 3:
            os.remove('session.txt')
            choices = False
            print()
        start = True
        print()                    
                             
else:
    start = True
