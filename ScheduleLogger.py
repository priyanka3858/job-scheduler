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

        dict = {}

        dict["headers"] = self.__format_str.format(self.__file_headers[0],
                                       self.__file_headers[1],
                                       (self.__file_headers[2]))

        dict["headerFormat"] = self.__format_str.format("-------", "--------", "---------")

        for i in list:
            dict[list.index(i)] = self.__format_str.format(list.index(i) + 1, str(i.time),
                                           i.name)
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

        # test_string = ""
        for i in list:
            # test_string = test_string + str(self.__format_str.format(list.index(i) + 1, str(i.time),i.name + "\r\n"))
            f.write(self.__format_str.format(list.index(i) + 1, str(i.time),
                                             i.name + "\r\n"))

        # print(test_string)
        # f.write("\r\n")
        f.close()

    def format_time(self):
        """ check Time format as HH:MM using datetime module """
        while True:
            try:
                time_prompt = input('specify time in HH:MM format: ')
                time = self.validate_time(time_prompt)
                break
            except:
                print("Please enter correct time in HH:MM format")
                continue
        return time

    def validate_time(self, time):
        """ check Time format as HH:MM using datetime module """
        return datetime.datetime.strptime(time, "%H:%M").time()
