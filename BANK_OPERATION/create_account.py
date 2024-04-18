print("welcome to online banking")
def create_account():
    global cname,cid,branch,balance


    print("for account creation")

    cname=input("enter your name")
    cid=int(input("enetr your id"))
    branch=input("enter the branch name")
    balance=int(input("enter the amount you want to enter in the account"))
    print("your account has been created")



def deposits():
    global balance
    deposit=int(input("enter the amount you want to add up in your balance"))
    balance=balance+deposit
    print("updated balance is",balance)

def withdraw():
    global balance
    wd=int(input("enter the amount you want to withdraw"))

    if(balance>=wd):
        balance = balance - wd
        print("withdrawal granted",wd)
    else:
        print("withdrawal not granted")

def display():
    print("customer name",cname)
    print("customer id",cid)
    print("branch of bank",branch)
    print("balance in the bank",balance)


print("Welcome to Online Banking")
create_account()

while(True):
    choice=int(input("Select ur Options 1: Deposite 2: Withdraw 3: Display 4: Exit"))
    if(choice==1):
        deposits()
    elif(choice==2):
        withdraw()
    elif(choice==3):
        display()
    elif(choice==4):
        exit(0)
    else:
        print("invalid choice")












