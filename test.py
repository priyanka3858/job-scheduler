from ScheduleLogger import ScheduleLogger
from SchedulerMenu import SchedulerMenu
from MyScheduler import MyScheduler

def test_add_to_scheduler():
    scheduler_list = []
    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Wake up", "6:00", scheduler_list)
    assert (scheduler_list[0].name == "Wake up")
    assert (scheduler_list[0].time == "6:00")

def test_remove_from_scheduler():
    scheduler_list = []

    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Wake up", "6:00", scheduler_list)
    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Exercise", "7:00", scheduler_list)


    '''
    After adding 2 activity to my scheduler, 
    
      Index      Time      Activity 
     -------    --------  --------- 
        1         06:00     Wake up  
        2         07:00     Exercise 
    '''

    scheduler_list = my_scheduler._MyScheduler__remove_from_myscheduler(1, scheduler_list)

    '''
    After removing number 1 activity from my scheduler, 

      Index      Time      Activity 
     -------    --------  --------- 
        1         07:00    Exercise 
    '''
    assert (scheduler_list[0].name == "Exercise")
    assert (scheduler_list[0].time == "7:00")


def test_change_scheduler():
    scheduler_list = []

    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Wake up",
                                                                   "6:00",
                                                                   scheduler_list)
    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Exercise",
                                                                   "7:00",
                                                                   scheduler_list)

    '''
    After adding 2 activity to my scheduler, 

      Index      Time      Activity 
     -------    --------  --------- 
        1         06:00     Wake up  
        2         07:00     Exercise 
    '''

    scheduler_list = my_scheduler._MyScheduler__change_myscheduler(2, "Breakfast", "6:30",
                                                                        scheduler_list)

    '''
    After changing number 2 activity from my scheduler, 

      Index      Time      Activity 
     -------    --------  --------- 
        1         06:30    Breakfast 
    '''
    assert (scheduler_list[1].name == "Breakfast")
    assert (scheduler_list[1].time == "6:30")

def test_format_output():
    scheduler_list = []

    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Wake up",
                                                                   "6:00",
                                                                   scheduler_list)
    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Exercise",
                                                                   "7:00",
                                                                   scheduler_list)

    schedular_format = schedule_logger.format_output(scheduler_list)

    assert (schedular_format == "Breakfast")

def test_write_to_file_output():
    scheduler_list = []

    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Wake up",
                                                                   "6:00",
                                                                   scheduler_list)
    scheduler_list = my_scheduler._MyScheduler__add_to_myscheduler("Exercise",
                                                                   "7:00",
                                                                   scheduler_list)

    schedular_format = schedule_logger.write_to_file(scheduler_list)

    '''
    after writing into text file the text file should look like this,
    
      Index      Time      Activity 
     -------    --------  --------- 
        1       06:00:00   Wake up  
        2       07:00:00  Excercise 
    '''


    file = open("myScheduler.txt", "r")
    Lines = file.readlines()
    Lines = [line.rstrip() for line in Lines]

    assert (Lines[0] == "  Index      Time     Activity")
    assert (Lines[1] == "=========   ========  ==========")
    assert (Lines[2] == "    1         6:00    Wake up")
    assert (Lines[3] == "     2         7:00    Exercise")



def test_validate_time():
    assert (schedule_logger.format_time() == "Breakfast")
    assert (schedule_logger.format_time() == "6:30")
    assert (schedule_logger.format_time() == "Breakfast")
    assert (schedule_logger.format_time() == "6:30")
    assert (schedule_logger.format_time()== "Breakfast")
    assert (schedule_logger.format_time() == "6:30")



if __name__ == '__main__':
    my_scheduler = MyScheduler("name", "time")
    schedule_logger = ScheduleLogger()

    test_add_to_scheduler()
    test_remove_from_scheduler()
    test_change_scheduler()
    # test_format_output()
    test_write_to_file_output()
    # test_validate_time()

    print("All assetionss Pass")
