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
            "Please enter command for your daily routine (example => add, "
                                                            "remove, change): ")

        try:
            # help command provide user to how to use instructs on command
            if user_inp.lower() == 'help':
                scheduler_menu.info_menu()
                continue

            # quit command for quit program
            if user_inp.lower() == 'quit':
                if len(scheduler_list) > 0:
                    print(
                        "Thank you for using Personal Daily Scheduler, Here is "
                        "your daily activiy and also daily actiivty saved in "
                        "text file.")
                    output_dict = schedule_logger.format_output(scheduler_list)
                    schedule_logger.printFormat(output_dict)
                    schedule_logger.write_to_file(scheduler_list)
                else:
                    print("Thank you for using Personal Daily Scheduler")
                break  # exit program

            # add command provide user to add time and activity name in schedule
            if user_inp.lower() == "add":
                user_inp = input("Enter your daily routine name: ")
                time_inp = schedule_logger.format_time()

                scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler(
                    user_inp, time_inp, scheduler_list)

                print(Colors.blue,
                      "Your schedule has been added to the list",
                      Colors.reset)

                output_dict = schedule_logger.format_output(scheduler_list)
                schedule_logger.printFormat(output_dict)
                continue

            # remove command provide user to remove data from schedule
            if user_inp.lower() == "remove":
                user_inp = input(
                    "Enter the number of schleulder you want to remove: ")

                scheduler_list =\
                    my_scheduler._MyScheduler__remove_from_myscheduler(
                    user_inp, scheduler_list)

                output_dict = schedule_logger.format_output(scheduler_list)
                schedule_logger.printFormat(output_dict)

                print(Colors.red,
                      "Schedule has been removed from the list",
                      Colors.reset)
                continue

            # change command provide user to modify data from schedule
            if user_inp.lower() == "change":
                index = input(
                    "Enter the number of scheduler that you want to change: ")
                user_inp_value = input("Enter name activity name to set:")
                time_inp_value = schedule_logger.format_time()

                scheduler_list = my_scheduler._MyScheduler__change_myscheduler(
                    index, user_inp_value, time_inp_value, scheduler_list)

                print(Colors.yellow,
                      "Your schedule has been updated",
                      Colors.reset)
                output_dict = schedule_logger.format_output(scheduler_list)
                schedule_logger.printFormat(output_dict)
                continue

        except:
            print( Colors.lightred, "Invalid input, please enter valid input",
                   Colors.reset)
            continue
        else:
            print(Colors.lightgrey, "Pleae enter Valid command, to see all the "
                                    "command please type 'help' ", Colors.reset)
            continue
