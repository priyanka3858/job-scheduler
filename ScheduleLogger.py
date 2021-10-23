import datetime
from SchedulerMenu import Colors

class ScheduleLogger():
    """ ScheduleLogger class contains handling methods for writing data to
    txt file """

    def __init__(self):
        """ file header name and format align center in txt file  """
        self.__file_headers = ("Index", "Time ", "Activity")
        self.__format_str = "{:^10} {:^10} {:^10}"

    def __add__(self, index):
        return int(index) + 1

    def format_output(self, list):
        """ file header set in text file using format method """

        dict = {}

        dict["headers"] = self.__format_str.format(self.__file_headers[0],
                                       self.__file_headers[1],
                                       (self.__file_headers[2]))

        dict["headerFormat"] = self.__format_str.format("-------", "--------",
                                                        "---------")

        for i in list:
            dict[list.index(i)] = self.__format_str.format(ScheduleLogger.
                            __add__(self, list.index(i)), str(i.time), i.name)
        return  dict

    def printFormat(self, dict):
        for v in dict.values():
            print(v)

    def write_to_file(self, list):
        """ Open myScheduler.txt and write file header and format and close
        the file"""
        f = open("myScheduler.txt", "w+")
        f.write(self.__format_str.format(self.__file_headers[0],
                                         self.__file_headers[1],
                                         (self.__file_headers[2] + "\r\n")))
        f.write(
            self.__format_str.format("=========", "========", "==========\r\n"))

        for i in list:
            f.write(self.__format_str.format(ScheduleLogger.__add__(self,
                                list.index(i)), str(i.time), i.name + "\r\n"))
        f.write("\r\n")
        f.close()

    def format_time(self):
        """ check Time format as HH:MM using datetime module """
        while True:
            try:
                time_prompt = input('Specify time in HH:MM (24 hour) format: ')
                time = self.validate_time(time_prompt)
                break
            except:
                print(Colors.lightred, "Please enter correct time in HH:MM "
                                            "(24 hour) format", Colors.reset)
                continue
        return time

    def validate_time(self, time):
        """ check Time format as HH:MM using datetime module """
        return datetime.datetime.strptime(time, "%H:%M").time()
