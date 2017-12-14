import datetime

def returnCurrentDate():
    currentdatetime = datetime.datetime.now()
    return (str(currentdatetime.day) + "/" + str(currentdatetime.month) + "/" + str(currentdatetime.year))
