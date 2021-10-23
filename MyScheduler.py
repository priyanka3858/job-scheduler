class MyScheduler():
    def __init__(self, name, time):
        """ init method """
        self.name = name
        self.time = time

    def __add_to_myscheduler(self, name, time, scheduler_list):
        """ __add_to_myscheduler method add name and time in scheduler_list"""
        scheduler_list.append(MyScheduler(name, time))
        return scheduler_list

    def __remove_from_myscheduler(self, index, scheduler_list):
        """ __remove_from_myscheduler method remove data from scheduler_list
        by index"""
        scheduler_list.pop(int(index) - 1)
        return scheduler_list

    def __change_myscheduler(self, index, name, time, scheduler_list):
        """ __change_from_myscheduler method change data from scheduler_list """
        scheduler_list[int(index) - 1] = MyScheduler(name, time)
        return scheduler_list
