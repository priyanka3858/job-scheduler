import datetime


class ScheduleLogger():
    """ ScheduleLogger class contains handling methods for writing data to
    txt file """

    def __init__(self):
        """ file header name and format align center in txt file  """
        self.__file_headers = ("Index", "Time ", "Activity")
        self.__format_str = "{:^10} {:^10} {:^10}"

    def format_output(self, list):
        """ file header set in text file using format method """
        print(self.__format_str.format(self.__file_headers[0],
                                       self.__file_headers[1],
                                       (self.__file_headers[2])))
        print(self.__format_str.format("-------", "--------", "---------"))
        for i in list:
            print(self.__format_str.format(list.index(i) + 1, str(i.time),
                                           i.name))

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
            f.write(self.__format_str.format(list.index(i) + 1, str(i.time),
                                             i.name + "\r\n"))
        f.write("\r\n")
        f.close()

    def format_time(self):
        """ check Time format as HH:MM using datetime module """
        while True:
            try:
                time = datetime.datetime.strptime(
                    input('specify time in HH:MM format: '), "%H:%M").time()
                break
            except:
                print("Please enter correct time in HH:MM format")
                continue
        return time
