import re
from datetime import datetime
from dateutil import parser, tz


NGINX_LINE_REGEXP = re.compile(
    ('(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
     ' - - '
     '\[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] '
     '((\"(?P<method>GET|POST|CONNECT|HEAD) )'
     '(?P<url>.+)(http\/1\.(1|0)")) '
     '(?P<statuscode>\d{3}) '
     '(?P<bytessent>\d+) '
     '(["](?P<refferer>(\-)|(.+))["]) '
     '(["](?P<useragent>.+)["])'), re.IGNORECASE)

DATE_TIME_FORMAT = '%d/%b/%Y:%H:%M:%S'
DATE_FORMAT = '%d/%m/%y'
TIME_FORMAT = '%H:%M:%S'
TIME_FORMAT2 = '%M:%S'
FIELDS = ['ip', 'date', 'time', 'method', 'url', 'status_code']
def main():

    status=[]
    i=0
    a=1
    count_status=[]
    with open('logs.txt') as f:
        for line in f.readlines():
            match = re.match(NGINX_LINE_REGEXP, line)
            if not match:
                continue
            log_datetime = match.group('dateandtime').replace(':', ' ', 1)
            log_datetime = parser.parse(log_datetime)
            utc_log_datetime = log_datetime.astimezone(tz.tzutc())
            parsed_item = {'ip': match.group('ipaddress'),
                           'date': utc_log_datetime.strftime(DATE_FORMAT),
                           'time': utc_log_datetime.strftime(TIME_FORMAT),
                           'method': match.group('method'),
                           'url': match.group('url'),
                           'status_code': match.group('statuscode')}
            if match.group('statuscode')=='403':
                print "Resources users tried to access without permissions is --", match.group('url'), match.group('statuscode')
            if match.group('statuscode')=='201':
                print "Created resources (HTTP status 201)--",match.group('url'), match.group('statuscode')
            status.append(match.group('statuscode'))
            if match.group('statuscode'):
                count_status.append(match.group('statuscode'))
            if match.group('statuscode')>='200' and match.group('statuscode')<='300':
                a+=1
            if utc_log_datetime.strftime(TIME_FORMAT2)>="15:11:00" and utc_log_datetime.strftime(TIME_FORMAT2)<="15:26:00":
                i+=1
        print 'Count requests in time range 15:11 - 15:26 is',i
        print set(status),"\n Count distinct status codes is",set(status).__len__()
        b=int(count_status.__len__())
        print a,b
        c=a*1.0/b
        print "Successful requests rate (2xx / all count)",c



if __name__ == '__main__':
    main()