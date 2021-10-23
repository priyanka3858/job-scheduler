class MyScheduler():
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __add_to_myscheduler(self, name, time, scheduler_list):
        scheduler_list.append(MyScheduler(name, time))
        return scheduler_list

    def __remove_from_myscheduler(self, index, scheduler_list):
        scheduler_list.pop(int(index) - 1)
        return scheduler_list

    def __change_myscheduler(self, index, name, time, scheduler_list):
        scheduler_list[int(index) - 1] = MyScheduler(name, time)
        return scheduler_list
