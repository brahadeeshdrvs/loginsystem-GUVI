# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import re
regex = r'\b[A-Za-z][A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def register ():
    username = username_check(input("enter the username:"))
    while True :
        password = input("enter the password:")
        if password_check(password):
            break;
            
    file = open('database.txt', 'a')
    file.write (username+','+password+'\n')
    
    



def username_check(username):
    file = open('database.txt', 'r')
    userdata = []
    for x in file :
        if ',' in x :
            user, passwd = x.split(',')
            userdata.append(user)
        if username not in userdata:
            if(re.fullmatch(regex,username)):
                print("Valid Email")
                return username
    
        else:
            print("Invalid Email")
            register()
    else:
        print('username already exists')
        register()
        
        
        
def password_check(passwd):
    
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 5:
        print('length should be at least 5')
        val = False
        
          
    if len(passwd) > 16:
        print('length should be not be greater than 15')
        val = False
        
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
        
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
       
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
        
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
        
    if val:
        return val
    
def login ():
    userlogin = input('enter the email ID:')
    userpwd = input ("enter your password:")
    file = open('database.txt', 'r')
    ran = True
    for x in file :
        if ',' in x :
            user,passwd = x.split(',')
        # print (passwd)
        if userlogin == user :
            ran = False
            if userpwd == passwd.strip() :
                print ('login success')
            else :
                print ('incorrect password')
                option= input('Enter 1 if you forgot password :\n Enter 2 for registering :')
                if option =='1':
                    forgot_password(userlogin)
                elif option == '2':
                    register()
                else:
                    print("invalid input")   
                
    if ran :
        
        print  ("User not found please register")
            
        
def forgot_password(username):
    file = open('database.txt', 'r')
    option = input("Enter 1 to retrieve old password : \n Enter 2 to change password :")
    for x in file :
        if ',' in x :
            user,passwd = x.split(',')
        if username == user :
            if option=='1':
                print("Your old password is "+ passwd)
            elif option=='2':
                while True :
                    newPassword = input("enter the password:")
                    if password_check(newPassword):
                        break;
                changePassword(username,passwd,newPassword)


def changePassword(username,oldPassword,newPassword):
    userinfo = (username+','+oldPassword)
    changeinfo = (username+','+newPassword)

    with open('database.txt','r') as file:
        print(file)
        data = file.read()

        print('data:'+data)
    data = data.replace(userinfo,changeinfo)

    with open('database.txt','w') as file:
        file.write(data)


             
main = input('Login Or Register:').lower()
if main == "login" :
    login()
elif main == "register" :
    register()








    
        
 