"""
Austin Salois, SCI220, Fall 2018
This script logs temperature and humidity at certain intervals and saves them to a data file
The data file output is in a common CSV format with a single header line.
"""


import time
import datetime

location_of_file='/Users/Ausitn/Desktop/Fall2018/Sci220/WeatherStation/'
name_of_file = str(datetime.date.today())
output_file = location_of_file + 'WeatherData;' + name_of_file + '.csv'

switch_state = False


def set_header():
    """
    This function adds the header line to the CSV file
    :param: None
    :return: None
    """
    file = open(output_file, 'a')
    string = 'Date, Time, Temperature, Humidity \n'
    file.write(string)
    file.close()
    return


def get_datetime():
    """
    This function gets the current date and time to use in the data output
    :param: None
    :return: date, time_out
    """
    time_read = str(datetime.datetime.now())
    space_index = time_read.find(' ')
    date = time_read[0:space_index-1]
    time_out = time_read[space_index+1:-1]
    return date, time_out


def write_to_file(string):
    """
    This function outputs a sting to the output file for data logging
    :param string: The combined output for the file
    :return: None
    """
    file_to_write = open(output_file, 'a')
    file_to_write.write(string)
    file_to_write.close()
    return


def get_temp_humidity():
    return


def get_switch_state():
    return


def main():
    set_header()
    i = 0
    get_switch_state()
    print(output_file)
    while i <= 10:
        date, time_now = get_datetime()
        print('The date is:', date)
        print('The time is:', time_now)
        string_to_write = date+','+time_now+'\n'
        write_to_file(string_to_write)
        time.sleep(1)
        i += 1


main()

