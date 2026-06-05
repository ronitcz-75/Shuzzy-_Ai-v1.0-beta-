#chatbot ai project

print("Chatbot: Hello user i am shuzzy here to help you. ")
Chatter=input("Chatbot: write message ?")
#first message concept 

def introduction(): #Introduction of chatbot () task 1
    inz=input("Chatbot: Yes ofcourse. to help you: ").strip()
    if inz =="what is your name":
        print("I am shuzzy ai to help you .") #——name is missing
    else:
        print("I don't know what you are saying")


def task_list(): #task 2
    inz1=input("Chatbot: I can do only calculation. ")
    if inz1=="do calculation":
        print("Chatbot: yes i can do:")
        user=input("So give me number?: ")# calculation task 1 
        if user=="yes":
            calc=int(input("Enter number: "))
            calc2=int(input("Enter second: "))
            perform=input("Perform task with number: ")
        if perform=="*":
           print(calc*calc2)
        if perform=="+":
           print(calc+clac2)
        elif perform=="-":
           print(calc-clac2)
        elif perform=="/":
           print(calc/calc2)
        else:
           print("Number can not perform any operation\n Please Enter valid number ")
 #Fallback mechanism 
if Chatter=="give me your introduction":
    print(introduction())
elif Chatter=="calculation":
    print(task_list())
else:
    print("I don't understand ask me ?")   
    #This ai model is incomeplete

def table_printer():
     chat=input("Chatbot:Any things you doubt I am here to solve?") #task 3
     if chat=="no":
         print("Chatbot:Ok no problem")
     ch=input("Chatbot:Ask me?")
     if ch=="hey print a table":
         print("Chatbot:Yes give me number?")
     num=int(input("Chatbot:Enter number?"))
     for i in range(1,11):
         print(f"{num} x {i}={num*i}")
#Fall back mechanism
if Chatter=="Table print":
    print(table_printer())