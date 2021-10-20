import functions
from class_file import MyScheduler


class Scheduler:
    print("Welcome to Personal Daily Scheduler.")

    scheduler_list=[]

    while True:

        # getting input from user
        user_inp = input("Please enter your daily routine: press 1 to add and 2 to delete, 3 modify 4 exit: ")

        try:
            if  int(user_inp) == 1:
                user_inp = input("enter your daily routine name: ")
                time = functions.format_time()
                scheduler_list.append(MyScheduler(user_inp, time))
                functions.format_output(scheduler_list)
                continue

            # check if length of input is 3 digit
            if int(user_inp) == 2:
                user_inp = input("enter the number of schleulder you want to remove: ")
                scheduler_list.pop(int(user_inp) - 1)
                functions.format_output(scheduler_list)
                continue

            if int(user_inp) == 3:
                user_inp = input("enter the number of schedulerthat you want to modify: ")
                user_inp_value = input("enter name activity name to set:")
                time = functions.format_time()
                scheduler_list[int(user_inp) - 1] = MyScheduler(user_inp_value,time)
                functions.format_output(scheduler_list)
                continue

            if int(user_inp) == 4:
                print("Thank you for using Personal Daily Scheduler, Here is your daily activiy and also daily actiivty saved in text file.")
                functions.write_to_file(scheduler_list)
                break # exit program
        except:
            print("Invalid input, please enter valid digit input")
            continue


