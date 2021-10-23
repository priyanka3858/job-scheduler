class SchedulerMenu:
    #My Scheduler App Menu start of the program and instructs on commands
    def __init__(self):
        print('\n')
        print(Colors.blue, Colors.bold, 'My Scheduler App', Colors.reset)
        print('-' * 60)
        print(Colors.bold, "My Scheduler App is personal daily scheduler will "
                           "help you to create and modify and track of your "
                           "daily schedule.", Colors.reset, '\n')

        print(Colors.lightgreen, "All available commands for input:",
              Colors.reset)
        print("="*40, '\n')
        print("     Type", Colors.green,"'add'", Colors.reset, "to add activity"
                                                        " in daily scheduler\n"
              "     Type", Colors.yellow,"'change'", Colors.reset,"to modify "
                                          "any activity from daily scheduler\n"
              "     Type", Colors.red,"'remove'", Colors.reset,"to remove "
                                             "activity from daily scheduler\n"
              "     Type", Colors.cyan,"'help'", Colors.reset,"to see all "
                                                        "options in Menu\n"
              "     Type", Colors.purple,"'quit'", Colors.reset,"to exit from "
                                                        "My Scheduler App\n")

        print(Colors.lightgreen, "EXAMPLE ====> To add activity in Scheduler:",
              Colors.reset)
        print("=" * 63)
        print("         To add activity in scheduler, type 'add', and prompt "
              "will ask you to input activity name & time. \n"
              ,"        Please enter command for your daily routine: "
               "Example ===> add, remove, change:", Colors.green,"add",
              Colors.reset)
        print("         Enter your daily routine name:", Colors.green,
              "Wake up", Colors.reset)
        print("         specify time in HH:MM format:", Colors.green,
              "06:00\n", Colors.reset)


    @staticmethod
    def info_menu():
        print("All available commands for input: \n")
        print("     Type", Colors.green, "'add'", Colors.reset,
              "to add activity in daily scheduler\n"
              "     Type", Colors.yellow, "'change'", Colors.reset,
              "to modify any activity from daily scheduler\n"
              "     Type", Colors.red, "'remove'", Colors.reset,
              "to remove any activity from daily scheduler\n"
              "     Type", Colors.cyan, "'help'", Colors.reset,
              "to see all options in Menu\n"
              "     Type", Colors.purple, "'quit'", Colors.reset,
              "to exit from My Scheduler App\n")

class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

