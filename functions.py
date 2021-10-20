import datetime

def format_output(list):
    format_str = "{:^10} {:^10} {:^10}"
    print(format_str.format("Index", "Time ", "Activity "))
    print(format_str.format("-------", "--------" , "---------"))
    for i in list:
        print(format_str.format(list.index(i) + 1, str(i.time), i.name))

def write_to_file(list):
    f = open("table.txt", "w+")
    format_str = "{:^10} {:^10} {:^10}"
    f.write(format_str.format("Index", "Time ", "Activity\r\n"))
    f.write(format_str.format("=========", "========", "==========\r\n"))
    for i in list:
        f.write(format_str.format(list.index(i) + 1, str(i.time), i.name + "\r\n"))
    f.write("\r\n")
    f.close()

def format_time():
    while True:
        try:
            time = datetime.datetime.strptime(input('specify time in HHMM format: '), "%H%M").time()
            break
        except:
            print("Please enter correct time in HHMM format")
            continue
    return time