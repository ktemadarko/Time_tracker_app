import datetime as dt
import time
import pandas as pd

#done is a variable used to intialize the while loop
done= False
tasks_info={}

print("Hello, Welcome to the Time and Pay Tracking App"
      "\nThis app allows you to track multiple tasks and calculate how much money was earned for each task. \nTo Start,\n")
user=input("Enter your name: ")
currency=input("Type the currency (in words) to be used for the calculations : ")

#while done== False the app will keep asking for input from the code in line 18.
#if the user enters done, the code jumps to the else statement in line 73 to exit the app

while not done:
    #Get task_title
    task_title= input("Type the task name to start the timer \nOr type done to exit the app: \n")

    if task_title.lower()!="done":
        print(f'Okay, the timer is running for Task {task_title}.')
        tasks_info["Task "+task_title]={}
        
        #Get Start_time
        start=str(dt.datetime.now()) #datetime is used to print the exact start time in the table
        format1 = '%Y-%m-%d %H:%M:%S.%f'
        start_dt = dt.datetime.strptime(start, format1)
        start_time=f'{start_dt.hour}:{start_dt.minute}:{start_dt.second}'
                
        s=time.perf_counter()        #perf_counter is used to get precision in seconds
        
        #Get Stop_time
        #validating that the user entered the key word stop to record the stop time
        check=False
        
        while not check:
            stop=input("\nType stop to halt the timer and record the time you ended Task "+ task_title + " :")
            if stop.lower()=="stop":
                end=str(dt.datetime.now()) #datetime is used to print the exact stop time in the table
                end_dt = dt.datetime.strptime(end, format1)
                end_time=f'{end_dt.hour}:{end_dt.minute}:{end_dt.second}'
                        
                e=time.perf_counter()    #perf_counter is used to get precision in seconds
                

                #Get duration, how long the person worked
                duration=round(float(e-s),4) #Time worked in seconds
                hours=round((duration/3600),4) #Time worked in hours

                #calculating money earned and validating answer
                
                while True:
                    Hourly_rate=input("\nEnter how much you earn per hour? ")
                    try:
                        int(Hourly_rate)
                        break;
                    except ValueError:
                        try:
                            float(Hourly_rate)
                            break;
                        except ValueError:
                            print("Please enter an integer or decimal.")
                        
                
                pay_rate_secs=float(Hourly_rate)/3600 #How much earned per second
                money=round(float(pay_rate_secs*duration),2)
                
                tasks_info["Task "+task_title]['A (Start_time)']=start_time 
                tasks_info["Task "+task_title]['B (Stop_time)']=end_time
                tasks_info["Task "+task_title]['C (Duration of Work in Seconds)']=duration
                
                tasks_info["Task "+task_title]['D (Duration of Work in Hours)']=hours
                tasks_info["Task "+task_title]['E (Hourly_pay_rate '+ currency+')']=Hourly_rate
                tasks_info["Task "+task_title]['F (Money_earned '+ currency+")"]=money
                
                print(f'\nGreat job, you worked for {working_hours} secs or {duration} secs or {hours}'
                      ' hours \nand have earned {money} {currency}.\n')
                check=True
        

    else: #end loop if done
        print(f"Okay, let's calculate how much {user} has earned.")
        tasks=pd.DataFrame.from_dict(tasks_info)
        Timesheet=tasks.T #transpose dataframe
        
        print(f"\nSince {user} earns {Hourly_rate} {currency} an hour. Here is your Timesheet.\n {Timesheet}"
             '\n\nDo you want to save the timesheet or just exit the app?')
        done=True
        
        #Checking if the user wants to save output in Excel file
        
save=False
while not save:
    output=input('Type save to create a Microsoft Excel file for your timesheet '
                 '\nOr type done to exit the app: ')

    if output.lower()=='save':
        Timesheet.to_excel("Time_Tracker_Python_output"+str(len(Timesheet))+".xlsx", engine="xlsxwriter")
        print("\nThat is it, check on your computer for a document called \nTime_Tracker_Python_output"
              +str(len(Timesheet))+".xlsx for your Timesheet in a Microsoft Excel file.")
        save=True
        
    elif output.lower()=="done":
        print(f"Have a great day {user}!")
        save=True
       
        
