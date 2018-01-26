from helper import spy_age,spy_name,spy_salutation,spy_rating
print("hello")
print("let's get started")
question = ("continue as " + spy_salutation + " " + spy_name + "(Y/N)?")
existing = input (question)

def start_chat(spy_name,spy_age,spy_rating):
    menu_choice = ("what do you want to do? \n 1. add a status update\n ")
    menu_choice = input (menu_choice)
    if( menu_choice == 1):
      print("status")

    else:
       pass
if(existing == "Y"):
    start_chat(spy_name,spy_age,spy_rating)
else:
 spy_name= input("welcome to spy chat,you must tell your spy name first")
 if len(spy_name) > 0:
     print("welcome" + spy_name + "glad to have you back with us")
     spy_salutation = input ("should i call you mister or miss?")
     spy_name = (spy_salutation+ " " + spy_name)
     print("alright" + "  " + spy_salutation + "  " + spy_name + "i would like to know a little bit more about you")
     spy_age = input ("what is your age?")
     if spy_age >12 and spy_age <50:
       print("valid spy")
       spy_rating = input("what is your spy rating")
       if spy_rating > 4.5:
          print("great ace!")
       elif spy_rating > 3.5 and spy_rating <=4.5:
          print("you are one of the good ones")

       elif spy_rating >=2.5 and spy_rating <= 3.5:
          print("you can always do better")
       else:
           print("we can always use somebody to help in the office")
       spy_is_online=True
       print("authentication complete. welcome " + "  "+spy_salutation+" "+ spy_name + "age:" + str(spy_age) + " and rating of: " +" proud to have you onboard")
     else:
       print("invalid age")
 else:
        print("please enter name")