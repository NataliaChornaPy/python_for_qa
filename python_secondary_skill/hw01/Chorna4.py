import sys
import json
from datetime import datetime, timedelta
from pprint import pprint


def get_dates_from_user():
    counter = True
    max_attempt_count = 3
    for attempt_number in range(max_attempt_count):
        if counter:
            usr_date = raw_input('\nTry {}.Please enter the date(2013-12-20):'.format(attempt_number))
            return usr_date


def get_sums(items_list, range_of_dates, item, condition):
    s = []
    # counter = True
    try:
        for target_date in range_of_dates:
            s = [items[item] for items in items_list if datetime.strptime(items[condition], '%Y-%m-%d').date().day == target_date.day]
            print target_date, '------', sum(s)
            counter = False
    except ValueError:
            print "Incorrect format - should be yyyy-mm-dd"
            counter = True
    return counter


def range_of_dates(usr_date):
    entered_dates = usr_date.split()
    list_dates = []
    for date in entered_dates:
        list_dates.append(datetime.strptime(date, '%Y-%m-%d').date())
    list_dates.sort()
    first_list_dates = list_dates[0]
    last_list_dates = list_dates[-1]
    for i in range(1, len(entered_dates)+1, 1):
        dates_before = first_list_dates - timedelta(days=i)
        dates_after = last_list_dates + timedelta(days=i)
        print type(dates_before)
        list_dates.append(dates_before)
        list_dates.append(dates_after)
    return list_dates

if __name__ == "__main__":
    file_path = sys.argv[1]
    dates = []
    with open(file_path) as data_file:
        data = json.load(data_file)
    # pprint (data)
    print '\nDATE_FROM:             ', data['DATE_FROM']
    print 'DATE TO:               ', (data['DATE_TO'])
    print 'STATION_CALL_LETTERS:  ', data["STATION"]['STATION_CALL_LETTERS']
    print 'STATION_NAME:          ', data["STATION"]['STATION_NAME'], '\n'

    dates = get_dates_from_user() # get one or two dates as entered by the user
    dates_list = range_of_dates(dates)
    sums = get_sums(data['ITEMS'], dates_list, 'HH', 'IMPRESSION_DATE')