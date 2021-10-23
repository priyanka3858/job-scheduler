class MyScheduler():
    def __init__(self, name, time):
        """ init method """
        self.name = name
        self.time = time

    def __sub__(self, index):
        return int(index) - 1

    def __add_to_myscheduler(self, name, time, scheduler_list):
        """ __add_to_myscheduler method add name and time in scheduler_list"""
        scheduler_list.append(MyScheduler(name, time))
        return scheduler_list


    def __remove_from_myscheduler(self, index, scheduler_list):
        """ __remove_from_myscheduler method remove data from scheduler_list
        by index"""
        scheduler_list.pop(MyScheduler.__sub__(self, index))
        return scheduler_list

    def __change_myscheduler(self, index, name, time, scheduler_list):
        """ __change_from_myscheduler method change data from scheduler_list """
        scheduler_list[MyScheduler.__sub__(self, index)] = MyScheduler(name,
                                                                       time)
        return scheduler_list

    def __repr__(self):
        """Return class description"""
        return 'Schedule to be added in the list is: (%s, %s)' % \
                                                    (self.name, self.time)