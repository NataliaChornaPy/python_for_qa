
from datetime import datetime,date
if __name__ == "__main__":
    fdat=['11 Jan 2016',"4 April 2011","11.03.2014","03/24/91","92.02.11"]
    print fdat
    for data in fdat:
     try:
        if data.find("/")>=0:
            f=datetime.strptime(data,'%m/%d/%y').date()
            print f

        elif data.find(".")>=0:
            f=datetime.strptime(data,'%d.%m.%Y').date()
            print f
        elif data.find(' '):
            tmp=data.split(' ')
            if tmp[1].__len__()==3:
                f=datetime.strptime(data,'%d %b %Y').date()
                print f
            else:
                f=datetime.strptime(data,'%d %B %Y').date()
                print f
        else:
            pass
     except ValueError:
         print "This date does not match format"