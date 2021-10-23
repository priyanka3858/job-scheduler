from ScheduleLogger import ScheduleLogger
from SchedulerMenu import SchedulerMenu
from MyScheduler import MyScheduler
from SchedulerMenu import Colors

if __name__ == '__main__':
    scheduler_menu = SchedulerMenu()
    schedule_logger = ScheduleLogger()
    my_scheduler = MyScheduler("name", "time")
    scheduler_list = []

    while True:
        """ getting input from user as add for add 'data' in schedule , 
        'remove' for remove data form schedule and 'change' for modify data 
        in schedule"""

        # input from user
        user_inp = input(
            "Please enter command for your daily routine: Example ===> add, remove, change: ")

        try:
            # help command provide user to how to use instructs on command
            if user_inp == 'help':
                scheduler_menu.info_menu()
                continue

            # quit command for quit program
            if user_inp == 'quit':
                if len(scheduler_list) > 0:
                    print(
                        "Thank you for using Personal Daily Scheduler, Here is your daily activiy and also daily actiivty saved in text file.")
                    schedule_logger.format_output(scheduler_list)
                    schedule_logger.write_to_file(scheduler_list)
                else:
                    print("Thank you for using Personal Daily Scheduler")
                break  # exit program

            # add command provide user to add time and activity name in schedule
            if user_inp == "add":
                user_inp = input("enter your daily routine name: ")
                time = schedule_logger.format_time()
                # scheduler_list.append(MyScheduler(user_inp, time))

                scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler(
                    user_inp, time, scheduler_list)

                print(Colors.FontColor.blue,
                      "Your schedule has been added to the list",
                      Colors.reset)

                schedule_logger.format_output(scheduler_list)
                continue

            # remove command provide user to remove data from schedule
            if user_inp == "remove":
                user_inp = input(
                    "Enter the number of schleulder you want to remove: ")

                # scheduler_list.pop(int(user_inp) - 1)

                scheduler_list = my_scheduler._MyScheduler__remove_from_myscheduler(
                    user_inp, scheduler_list)

                schedule_logger.format_output(scheduler_list)
                print(Colors.FontColor.red,
                      "schedule has been removed from the list",
                      Colors.reset)
                continue

            # change command provide user to modify data from schedule
            if user_inp == "change":
                index = input(
                    "enter the number of scheduler that you want to change: ")
                user_inp_value = input("enter name activity name to set:")
                time = schedule_logger.format_time()

                scheduler_list = my_scheduler._MyScheduler__change_myscheduler(
                    index, user_inp_value, time, scheduler_list)

                # scheduler_list[int(user_inp) - 1] = MyScheduler(user_inp_value, time)

                print(Colors.FontColor.yellow,
                      "your schedule has been updated",
                      Colors.reset)
                schedule_logger.format_output(scheduler_list)
                continue
        except:
            print("Invalid input, please enter valid input")
            continue
