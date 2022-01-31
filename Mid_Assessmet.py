log = {}
outputs = []


class Logger:
    def shouldPrintMessage(self, timestamp, message):
        if message in log.keys():
            if log[message] + 10 <= timestamp:
                outputs.append("True")
                log[message] = timestamp
            else:
                outputs.append("False")
        else:
            log[message] = timestamp
            outputs.append("True")


logger = Logger()

while 1:
    time_input = input("Enter timestamp or q to quit ")
    if time_input.lower() != 'q':
        mess = input("Enter your message or q to quit ")
    if (time_input.lower() == 'q') | (mess.lower() == 'q'):
        break
    if (time_input == '') | (mess == ''):
        outputs.append("Null")
    else:
        time = int(time_input)
        logger.shouldPrintMessage(time, mess)

for out in outputs:
    print(out)
