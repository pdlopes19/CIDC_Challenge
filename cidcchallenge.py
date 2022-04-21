# _______________________________________________________________________________ #
#                                                                                 #
# [ CIDC Challenge - Building a report through a spread sheet ]                    #
#                                                                                 #
# -> Pedro Lopes de Oliveira - Undergraduated Telecommunications Engineer         #
# -> Yara Caroline Tavares Mendes - Undergraduated Telecommunications Engineer    #
#                                                                                 #
# _______________________________________________________________________________ #
#                                                                                 #
#
# To receive good results, please pip install all modules below.
#
# pip install pandas
# pip install matplotlib
# pip install numpy
# pip install openpyxl
# pip install PyQt5
# pip install xlrd

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import time
import os
from PyQt5.QtWidgets import QApplication, QDialog


# Conversion .xls -> .csv
def archive_conversion(archive_name):
    # Reading .xls archive and converting into a .csv archive ( that format is better when dealing with pandas )
    read_file = pd.read_excel(archive_name + '.xlsx')
    read_file.to_csv(archive_name + '.csv', index=None, header=True)


# Operators class englobe an amount of functions that do operations envolving operators of the spread sheet
class Operators(object):
    data_frame = None
    operators_list = None
    number_of_services = None
    number_of_unique_services_per_operator = None
    services_obj = None
    services_list = None
    operators_mean = None

    # Class inicialization
    def __init__(self, archive_name):

        self.data_frame = pd.read_csv(archive_name + '.csv')

        self.operators_list = list(self.data_frame['Account'].unique())

        self.number_of_services = {}
        self.number_of_unique_services_per_operator = {}

        self.services_obj = Services(archive_name)
        self.services_list = self.services_obj.show_services(1)

        self.operators_mean = {}

        for i in self.operators_list:
            self.operators_mean[i] = 0

        for i in self.operators_list:

            self.number_of_services[str(i)] = 0

            for j in self.services_list:
                self.number_of_unique_services_per_operator[str(i) + ' + ' + str(j)] = 0

    # Return the list of operators, when flag is equals 0 the function print the operators list too.
    def show_operators(self, flag=0):

        if flag == 0:

            #print('\n[Operators list]\n')

            #for i in range(0, len(self.operators_list)):
                #print('[{}] {} '.format(i + 1, self.operators_list[i]))

            return self.operators_list

        else:

            return self.operators_list

    # Do the count of services did per operator, also print it and return.
    def count_number_of_services(self):

        #print('\n[Services per operator considering outliers]\n')

        for i in self.operators_list:

            self.number_of_services[str(i)] = len(self.data_frame[self.data_frame['Account'] == str(i)])

            #print('{}: {}'.format(i, self.number_of_services[str(i)]))

        return self.number_of_services

    # Do the count of unique services did per operator, also print it and return.
    def count_number_of_unique_services_per_operator(self):

        filtro1 = 'Account'
        filtro2 = 'Activity Type'

        #print('\n[Unique services per operator considering outliers]\n')

        number_of_unique_services_per_operator_temp = {}

        for i in self.operators_list:

            for j in self.services_list:

                number_of_unique_services_per_operator_temp[str(i) + ' + ' + str(j)] = len(
                    self.data_frame[(self.data_frame[filtro1] == str(i)) & (self.data_frame[filtro2] == str(j))])

                self.number_of_unique_services_per_operator[str(i) + ' + ' + str(j)] = len(
                self.data_frame[(self.data_frame[filtro1] == str(i)) & (self.data_frame[filtro2] == str(j))])
                #print('{} + {}: {}'.format(i, j, self.number_of_unique_services_per_operator[str(i) + ' + ' + str(j)]))

        print(number_of_unique_services_per_operator_temp)

        return number_of_unique_services_per_operator_temp

    # Calculate the mean duration of activities did to a certain operator.
    def calc_operators_mean_duration(self, data_frame):

        ##print('\n[Mean duration for each operator]\n')

        for i in self.operators_list:
            data_frame_temp = data_frame[data_frame['Operator'] == str(i)]
            self.operators_mean[i] = round(data_frame_temp['Duration [s]'].mean(), 2)
            #print('Mean of {}: {} [s]'.format(i, self.operators_mean[i]))

        return self.operators_mean

    def count_number_of_services_without_outlier(self, data_frame_temp):

        #print('\n[Services per operator desconsidering outliers]\n')

        number_of_services_temp = {}

        for i in self.operators_list:

            number_of_services_temp[str(i)] = 0

        for i in self.operators_list:

            number_of_services_temp[str(i)] = len(data_frame_temp[data_frame_temp['Operator'] == str(i)])

            #print('{}: {}'.format(i, number_of_services_temp[str(i)]))

        return number_of_services_temp

    # Do the count of unique services did per operator, also print it and return.
    def count_number_of_unique_services_per_operator_without_outlier(self, data_frame_temp):

        filtro1 = 'Operator'
        filtro2 = 'Activity'

        #print('\n[Unique services per operator desconsidering outliers]\n')

        number_of_unique_services_per_operator_temp = {}

        for i in self.operators_list:
            for j in self.services_list:
                self.number_of_unique_services_per_operator[str(i) + ' + ' + str(j)] = 0

        for i in self.operators_list:

            for j in self.services_list:

                number_of_unique_services_per_operator_temp[str(i) + ' + ' + str(j)] = len(
                data_frame_temp[(data_frame_temp[filtro1] == str(i)) & (data_frame_temp[filtro2] == str(j))])

                #print('{} + {}: {}'.format(i, j, number_of_unique_services_per_operator_temp[str(i) + ' + ' + str(j)]))

        print(number_of_unique_services_per_operator_temp)
        return number_of_unique_services_per_operator_temp


# Services class englobe an amount of functions that do operations envolving services of the spread sheet
class Services(object):

    data_frame = None
    services_list = None
    number_of_unique_services = None
    services_mean = None

    # Class inicialization
    def __init__(self, archive_name):

        self.data_frame = pd.read_csv(archive_name + '.csv')

        self.services_list = list(self.data_frame['Activity Type'].unique())

        self.number_of_unique_services = {}

        for i in self.services_list:
            self.number_of_unique_services[str(i)] = 0

        self.services_mean = {}

        for i in self.services_list:
            self.services_mean[str(i)] = 0

    # Return the list of services, when flag is equals 0 the function print the services list too.
    def show_services(self, flag=0):

        if flag == 0:

            #print('\n[Services list]\n')

            #for i in range(0, len(self.services_list)):
                #print('[{}] {} '.format(i + 1, self.services_list[i]))

            return self.services_list

        else:

            return self.services_list

    # Do the count of unique services did, also return and print it
    def count_number_of_unique_services(self):

        #print('\n[Unique services considering outliers]\n')

        for i in self.services_list:

            self.number_of_unique_services[str(i)] = len(self.data_frame[self.data_frame['Activity Type'] == str(i)])
            #print('{}: {}'.format(i, self.number_of_unique_services[str(i)]))

        return self.number_of_unique_services

    def count_number_of_unique_services_without_outlier(self, data_frame_temp):

        #print('\n[Unique services desconsidering outliers]\n')

        number_of_unique_services_temp = {}

        for i in self.services_list:
            number_of_unique_services_temp[str(i)] = 0

        for i in self.services_list:

            number_of_unique_services_temp[str(i)] = len(data_frame_temp[data_frame_temp['Activity'] == str(i)])
            #print('{}: {}'.format(i, number_of_unique_services_temp[str(i)]))

        return number_of_unique_services_temp

    # Calculate the mean duration per service
    def calc_services_mean_duration(self, data_frame):

        #print('\n[Mean duration for each service]\n')

        for i in self.services_list:
            data_frame_temp = data_frame[data_frame['Activity'] == str(i)]
            self.services_mean[i] = round(data_frame_temp['Duration [s]'].mean(),2)
            #print('Mean of {}: {} [s]'.format(i, self.services_mean[i]))

        return self.services_mean


# Employees class englobe an amount of functions that do operations envolving employees of the spread sheet
class Employees(object):

    data_frame = None
    data_frame_employees = None
    data_frame_employees_without_outlier = None

    employees_list = None
    employees_time = None
    employees_mean = None

    above_mean_employees = None
    below_mean_employees = None
    above_mean_employees_without_outlier = None
    below_mean_employees_without_outlier = None

    # Class inicialization
    def __init__(self, archive_name):

        self.data_frame = pd.read_csv(archive_name + '.csv')

        self.employees_list = list(self.data_frame['Assigned to'].unique())

        self.above_mean_employees = {}
        self.below_mean_employees = {}
        self.above_mean_employees_without_outlier = {}
        self.below_mean_employees_without_outlier = {}

        for i in self.employees_list:
            self.above_mean_employees[i] = 0
            self.below_mean_employees[i] = 0
            self.above_mean_employees_without_outlier[i] = 0
            self.below_mean_employees_without_outlier[i] = 0

        self.employees_mean = {}

        for i in self.employees_list:
            self.employees_mean[i] = 0



    # Return the list of employees, when flag is equals 0 the function print the employees list too.
    def show_employees(self, flag=0):

        if flag == 0:

            #print('\n[Employees list]\n')

            #for i in range(0, len(self.employees_list)):
                #print('[{}] {} '.format(i + 1, self.employees_list[i]))

            return self.employees_list

        else:

            return self.employees_list

    # Calculate the above and below mean employees, considering the outliers, organize them in a dataframe for better visualization of which activity exceeded the mean time
    def calc_above_below_mean_employees_with_outlier(self, mean_with_outlier, information):

        above_mean = []
        name = information[0]
        timestamp = information[1]
        task = information[2]
        activity = information[3]
        operator = information[4]

        for i in range(0, len(name)):

            if timestamp[i] >= mean_with_outlier:

                above_mean.append('Yes')
                self.above_mean_employees[name[i]] += 1

            else:

                above_mean.append('No')
                self.below_mean_employees[name[i]] += 1

        self.data_frame_employees = pd.DataFrame()

        self.data_frame_employees['Employee'] = name
        self.data_frame_employees['Above mean?'] = above_mean
        self.data_frame_employees['Duration [s]'] = timestamp
        self.data_frame_employees['Task'] = task
        self.data_frame_employees['Activity'] = activity
        self.data_frame_employees['Operator'] = operator

        #print("\n[Employees' duration mean ( with outliers )] \n")
        #print(self.data_frame_employees)

        #print('[Employees above mean X times ( with outliers )]\n')

        log = '[Employees above mean X times ( with outliers )]\n\n'

        for i in self.employees_list:
            log += '[ {} ] Above mean {} times.\n'.format(i, self.above_mean_employees[i])
            #print('[ {} ] Above mean {} times.'.format(i, self.above_mean_employees[i]))

        #print('\n[Employees below mean X times ( with outliers )]\n')
        log += '\n[Employees below mean X times ( with outliers )]\n\n'

        for i in self.employees_list:
            log += '[ {} ] Below mean {} times.\n'.format(i, self.below_mean_employees[i])
            #print('[ {} ] Below mean {} times.'.format(i, self.below_mean_employees[i]))

        self.data_frame_employees.to_excel('data_frames\Data frame employees - with outliers.xlsx')

        arquivo = open('text_archives\Report employees - with outliers.txt', 'w')
        arquivo.write(log)
        arquivo.close()

        return self.data_frame_employees

    # Calculate the above and below mean employees, desconsidering the outliers, organize them in a dataframe for better visualization of which activity exceeded the mean time
    def calc_above_below_mean_employees_without_outlier(self, mean_without_outlier, data_frame):

        above_mean = []
        name = list(data_frame['Employee'])
        timestamp = list(data_frame['Duration [s]'])
        task = list(data_frame['Task'])
        activity = list(data_frame['Activity'])
        operator = list(data_frame['Operator'])

        for i in range(0, len(name)):

            if timestamp[i] >= mean_without_outlier:

                above_mean.append('Yes')
                self.above_mean_employees_without_outlier[name[i]] += 1

            else:

                above_mean.append('No')
                self.below_mean_employees_without_outlier[name[i]] += 1

        self.data_frame_employees_without_outlier = pd.DataFrame()

        self.data_frame_employees_without_outlier['Employee'] = name
        self.data_frame_employees_without_outlier['Above mean?'] = above_mean
        self.data_frame_employees_without_outlier['Duration [s]'] = timestamp
        self.data_frame_employees_without_outlier['Task'] = task
        self.data_frame_employees_without_outlier['Activity'] = activity
        self.data_frame_employees_without_outlier['Operator'] = operator

        #print("\n[Employees' duration mean ( without outliers )]\n")
        #print(self.data_frame_employees_without_outlier)

        #print('\n[Employees above mean X times ( without outliers )]\n')

        log = '[Employees above mean X times ( without outliers )]\n\n'

        for i in self.employees_list:
            log += '[ {} ] Above mean {} times.\n'.format(i, self.above_mean_employees_without_outlier[i])
            #print('[ {} ] Above mean {} times.'.format(i, self.above_mean_employees_without_outlier[i]))

        #print('\n[Employees below mean X times ( without outliers )]\n')

        log += '\n[Employees below mean X times ( without outliers )]\n\n'

        for i in self.employees_list:
            log += '[ {} ] Below mean {} times.\n'.format(i, self.below_mean_employees_without_outlier[i])
            #print('[ {} ] Below mean {} times.'.format(i, self.below_mean_employees_without_outlier[i]))

        self.data_frame_employees_without_outlier.to_excel('data_frames\Data frame employees - without outliers.xlsx')

        arquivo = open('text_archives\Report employees - without outliers.txt', 'w')
        arquivo.write(log)
        arquivo.close()

        return self.data_frame_employees_without_outlier


    # Calculate the mean duration per employee on execution of activities
    def calc_mean_duration_per_employee(self, data_frame):

        #print('\n[Mean duration for each employee]\n')

        for i in self.employees_list:
            data_frame_temp = data_frame[data_frame['Employee'] == str(i)]
            self.employees_mean[i] = round(data_frame_temp['Duration [s]'].mean(), 2)
            #print("{}'s Mean: {} [s]".format(i, self.employees_mean[i]))

        return self.employees_mean

# Info class englobe an amount of functions that do operations envolving the principal parameters of the spread sheet, like mean and standard deviation of the general duration
class Info(object):

    data_frame = None
    operators_list = None
    services_list = None
    employees_list = None

    operators_obj = None
    services_obj = None
    employees_obj = None

    # Class inicialization
    def __init__(self, archive_name):

        archive_conversion(archive_name)
        self.data_frame = pd.read_csv(archive_name + '.csv')

        self.operators_obj = Operators(archive_name)
        self.services_obj = Services(archive_name)
        self.employees_obj = Employees(archive_name)

    # Call all basic functions that returns little informations about the spreadsheet
    def show_basic_info(self):

        self.operators_obj.show_operators()
        self.services_obj.show_services()
        self.employees_obj.show_employees()

    # Call all functions in Operators class that do calcs
    def calc_number_info_operators(self):

        self.operators_obj.count_number_of_services()
        self.operators_obj.count_number_of_unique_services_per_operator()

    # Call all functions in Services class that do calcs
    def calc_number_info_services(self):

        self.services_obj.count_number_of_unique_services()

    # Call all functions in Employees class that do calcs that envolve outliers
    def calc_number_info_employees_with_outlier(self, mean_with_outlier, timestamps_employees):

        self.employees_obj.calc_above_below_mean_employees_with_outlier(mean_with_outlier, timestamps_employees)

    # Call all functions on Employees class that do calcs that do not envolve outliers
    def calc_number_info_employees_without_outlier(self, mean_without_outlier, information):

        self.employees_obj.calc_above_below_mean_employees_without_outlier(mean_without_outlier, information)

    # Save and show histograms to have an idea of general times distribution desconsidering outliers
    def show_graphic_without_outliers(self, timestamps, mean, std):

        x = list(timestamps)

        mean = time.strftime('%H:%M:%S', time.gmtime(mean))
        std = time.strftime('%H:%M:%S', time.gmtime(std))

        n, bins, patches = plt.hist(x, density=True, alpha=1)

        plt.xlabel('Timestamp [s]')
        plt.title("General timestamps' histogram [ without outliers ]")
        plt.text(2500, .00012,
                 r'$\mu={},\ \sigma={}$'.format(mean, std))
        plt.xlim(0, 40000)
        plt.grid(True)
        plt.savefig("graphics\General timestamps' histogram desconsidering outliers.pdf")
        plt.show()

    # Save and show histograms to have an idea of general times distribution considering outliers
    def show_graphic_with_outliers(self, timestamps, mean, std):

        x = timestamps

        mean = time.strftime('%H:%M:%S', time.gmtime(mean))
        std = time.strftime('%H:%M:%S', time.gmtime(std))

        n, bins, patches = plt.hist(x, density=True, alpha=1)

        plt.xlabel('Timestamp [s]')
        plt.title("General timestamps' histogram [ with outliers ]")
        plt.text(20000, .00005,
                 r'$\mu={},\ \sigma={}$'.format(mean, std))
        plt.xlim(0, 40000)
        plt.grid(True)
        plt.savefig("graphics\General timestamps' histogram considering outliers.pdf")
        plt.show()

    def show_graphic_operators(self, operators_number_of_services, flag):

        bars = []
        height = []

        for i in self.operators_obj.operators_list:

            bars.append(i)
            height.append(operators_number_of_services[i])

        y_pos = np.arange(len(bars))

        plt.title('Operators distribution ' + flag )
        plt.bar(y_pos, height, width=0.5)
        plt.grid(True)
        plt.savefig('graphics\Operators distribution ' + flag + '.pdf')
        plt.xticks(y_pos, bars)
        plt.show()

    def show_graphic_operators_unique_services(self, operators_number_of_unique_services, flag):

        bars = []

        zaz = []
        wow = []

        for i in self.operators_obj.operators_list:

            for j in self.services_obj.services_list:

                key = str(i) + ' + ' + str(j)

                if i == 'ZAZ Telecom':

                    zaz.append(operators_number_of_unique_services[key])

                else:

                    wow.append(operators_number_of_unique_services[key])

        for i in self.services_obj.services_list:

            bars.append(i)

        print(bars)
        print(zaz)
        print(wow)

        y_pos = np.arange(len(bars))

        plt.title('Unique services distribution ' + flag + ' ( ZAZ Telecom )')
        plt.bar(y_pos, zaz, width=0.5)
        plt.xticks(y_pos, bars, rotation=90, fontsize = 6)
        plt.grid(True)
        plt.show()
        plt.savefig("graphics\XUnique services distribution " + flag + ' ( ZAZ Telecom ).pdf')
        plt.close()

        plt.title('Unique services distribution ' + flag + ' ( WOW Telecom )')
        plt.bar(y_pos, wow, width=0.5)
        plt.xticks(y_pos, bars, rotation = 90, fontsize = 6)
        plt.grid(True)
        plt.show()
        plt.savefig('graphics\XUnique services distribution ' + flag + ' ( WOW Telecom ).pdf')

    def show_graphic_operators_mean(self, operators_mean, flag):

        height = []
        bars = []

        for i in self.operators_obj.operators_list:

            bars.append(i)
            height.append(operators_mean[i])

        y_pos = np.arange(len(bars))

        plt.title('Operators mean ' + flag)
        plt.bar(y_pos, height, width=0.5)
        plt.ylabel('Timestamp [s]')
        plt.grid(True)
        plt.savefig('graphics\Operators mean ' + flag + '.pdf')
        plt.xticks(y_pos, bars)
        plt.show()

    def show_graphic_services_mean(self, services_mean, flag):

        height = []
        bars = []

        for i in self.operators_obj.operators_list:

            bars.append(i)
            height.append(services_mean[i])

        y_pos = np.arange(len(bars))

        plt.title('Services mean ' + flag)
        plt.bar(y_pos, height, width=0.5)
        plt.ylabel('Timestamp [s]')
        plt.grid(True)
        plt.savefig('graphics\Services mean ' + flag + '.pdf')
        plt.xticks(y_pos, bars, rotation=90, fontsize = 6)
        plt.show()

    def show_graphic_services_unique(self, unique_services, flag):

        height = []
        bars = []

        for i in self.services_obj.services_list:
            bars.append(i)
            height.append(unique_services[i])

        y_pos = np.arange(len(bars))

        plt.title('Unique services ' + flag)
        plt.bar(y_pos, height, width=0.5)
        plt.ylabel('Timestamp [s]')
        plt.grid(True)
        plt.savefig('graphics\XUnique services ' + flag + '.pdf')
        plt.xticks(y_pos, bars, rotation = 90, fontsize = 6)
        plt.show()

    def show_graphic_employees_mean(self, employees_mean, mean_wo, std_wo):

        height = []
        bars = []

        # for i in self.employees_obj.employees_list:
        #     bars.append(i)
        #     height.append(employees_mean[i])
        #
        # mean_wo = time.strftime('%H:%M:%S', time.gmtime(mean_wo))
        # std_wo = time.strftime('%H:%M:%S', time.gmtime(std_wo))
        #
        # y_pos = np.arange(len(bars))
        #
        # plt.title('Employees mean')
        # plt.bar(y_pos, height, width=0.5)
        # plt.ylabel('Timestamp [s]')
        # plt.grid(True)
        # plt.text(0, 14000,
        #          r'$\mu={}\ \sigma = {}$'.format(mean_wo, std_wo), fontsize = 10)
        # plt.savefig('graphics\Employees mean.pdf')
        # plt.xticks(y_pos, bars)
        # plt.show()

        threshold = mean_wo

        for i in self.employees_obj.employees_list:

            bars.append(i)
            height.append(employees_mean[i])

        # split it up
        above_threshold = np.maximum(height - threshold, 0)
        below_threshold = np.minimum(height, threshold)

        x = self.employees_obj.employees_list

        # and plot it
        fig, ax = plt.subplots()
        ax.bar(x, below_threshold)
        ax.bar(x, above_threshold, bottom=below_threshold)

        # horizontal line indicating the threshold
        ax.plot([-10, 10], [threshold, threshold], "black")
        plt.xlim(-0.5, 3.5)
        plt.grid()

        mean_wo = time.strftime('%H:%M:%S', time.gmtime(mean_wo))
        std_wo = time.strftime('%H:%M:%S', time.gmtime(std_wo))

        plt.text(-0.3, 14000, r'$\mu={}\ \sigma = {}$'.format(mean_wo, std_wo), fontsize = 10)
        plt.ylabel('Timestamps [s]')

        plt.savefig('graphics\Employees mean.pdf')
        plt.show()

# Spreadsheet class englobe an amount of functions that make transformations on the spreadsheet which will garantee easiest operations
class Spreadsheet(Info):

    data_frame_timestamp = None
    data_frame_timestamp_without_outliers = None
    data_frame_employees_without_outliers = None
    timestamps = None
    timestamps_without_outliers = None

    employees_column = None
    employees_column_without_outliers = None
    employees_timestamps = None
    employees_timestamps_without_outliers = None
    employees_tasks = None
    employees_activities = None
    employees_operator = None
    employees_tasks_without_outliers = None
    employees_activities_without_outliers = None
    employees_operator_without_outliers = None

    standard_deviation_with_outlier = None
    standard_deviation_without_outlier = None
    mean_with_outlier = None
    mean_without_outlier = None

    # Class inicialization
    def __init__(self, archive_name):

        super().__init__(archive_name)

        self.data_frame_timestamp = pd.read_csv(archive_name + '.csv')
        self.employees_timestamps = {}
        self.employees_timestamps_without_outliers = {}
        self.employees_column = list(self.data_frame['Assigned to'])
        self.employees_activities = list(self.data_frame['Activity Type'])
        self.employees_operator = list(self.data_frame['Account'])
        self.employees_tasks = list(self.data_frame['Task'])
        self.employees_list = self.employees_obj.show_employees(1)
        self.data_frame_employees_without_outliers = pd.DataFrame()

    # Conversion : Duration on hour format of activities -> Duration on timestamp of activities
    def timestamp_conversion(self):

        hour_format = list(self.data_frame_timestamp['Duration'])
        self.timestamps = list()

        for i in hour_format:

            if i[0] == '-' and len(i) == len('-x:xx:xx'):

                conversion = int(i[1]) * 3600 + int(i[3] + i[4]) * 60 + int(i[6] + i[7])
                self.timestamps.append(conversion)

            elif i[0] == '-' and len(i) == len('-xx:xx:xx'):

                conversion = int(i[1] + i[2]) * 3600 + int(i[4] + i[5]) * 60 + int(i[7] + i[8])
                self.timestamps.append(conversion)

            else:

                conversion = int(i[0] + i[1]) * 3600 + int(i[3] + i[4]) * 60 + int(i[6] + i[7])
                self.timestamps.append(conversion)

        self.data_frame_timestamp['Timestamps'] = self.timestamps

        return self.timestamps

    # Designation of timestamps to each employee
    def timestamp_designation(self):

        names_designation_list = []
        timestamps_designation_list = []
        task = list(self.data_frame['Task'])
        activity = list(self.data_frame['Activity Type'])
        operator = list(self.data_frame['Account'])
        information = []

        for j in self.employees_list:

            for i in range(0, len(self.employees_column)):

                if self.employees_column[i] == j:
                    name = j
                    timestamp = self.timestamps[i]
                    names_designation_list.append(name)
                    timestamps_designation_list.append(timestamp)

        information.append(names_designation_list)
        information.append(timestamps_designation_list)
        information.append(task)
        information.append(activity)
        information.append(operator)

        return information

    # Calculate the standard deviation, considering outliers, of the duration of all activities
    def calc_std_deviation_with_outlier(self):

        self.standard_deviation_with_outlier = round(self.data_frame_timestamp['Timestamps'].std(), 4)
        #print('\nStandard Deviation with outlier: {}'.format(self.standard_deviation_with_outlier))

        return self.standard_deviation_with_outlier

    # Calculate the mean, considering outliers, of the duration of all activities
    def calc_mean_with_outlier(self):

        self.mean_with_outlier = round(self.data_frame_timestamp['Timestamps'].mean(), 4)
        #print('Mean with outlier: {}'.format(self.mean_with_outlier))

        return self.mean_with_outlier

    # Creation of a data frame, considering an outlier pattern, that have only durations between an interval
    def exclude_outliers(self, outlier_pattern):

        outlier_pattern_times = outlier_pattern * self.standard_deviation_with_outlier
        outlier_pattern_split = self.standard_deviation_with_outlier / outlier_pattern

        #print('\n[Outlier pattern fix]\n')
        #print('Outlier if Timestamp > Standard Deviation * {} = {}'.format(outlier_pattern, round(outlier_pattern_times, 2)))
        #print('or')
        #print('Outlier if Timestamp < Standard Deviation / {} = {}'.format(outlier_pattern, round(outlier_pattern_split, 2)))

        self.data_frame_employees_without_outliers = pd.DataFrame()

        cont = 0
        cont_outliers = 0
        self.employees_column_without_outliers = []
        self.timestamps_without_outliers = []
        self.employees_activities_without_outliers = []
        self.employees_tasks_without_outliers = []
        self.employees_operator_without_outliers = []

        for i in self.timestamps:

            if not (i < outlier_pattern_split or i > outlier_pattern_times):


                self.timestamps_without_outliers.append(i)
                self.employees_column_without_outliers.append(self.employees_column[cont])
                self.employees_tasks_without_outliers.append(self.employees_tasks[cont])
                self.employees_operator_without_outliers.append(self.employees_operator[cont])
                self.employees_activities_without_outliers.append(self.employees_activities[cont])

            else:

                cont_outliers += 1

            cont += 1

        self.data_frame_timestamp_without_outliers = pd.DataFrame()
        self.data_frame_timestamp_without_outliers['Timestamps'] = self.timestamps_without_outliers

        self.data_frame_employees_without_outliers['Employee'] = self.employees_column_without_outliers
        self.data_frame_employees_without_outliers['Duration [s]'] = self.timestamps_without_outliers
        self.data_frame_employees_without_outliers['Task'] = self.employees_tasks_without_outliers
        self.data_frame_employees_without_outliers['Activity'] = self.employees_activities_without_outliers
        self.data_frame_employees_without_outliers['Operator'] = self.employees_operator_without_outliers

        #print('\nNumber of outliers: {}'.format(cont_outliers))

        return self.data_frame_employees_without_outliers

    # Calculate the standard deviation, desconsidering outliers, of the duration of all activities
    def calc_std_deviation_without_outlier(self):

        self.standard_deviation_without_outlier = round(self.data_frame_timestamp_without_outliers['Timestamps'].std(),
                                                        4)
        #print('\nStandard Deviation without outlier: {}'.format(self.standard_deviation_with_outlier))

        return self.standard_deviation_without_outlier

    # Calculate the mean, desconsidering outliers, of the duration of all activities
    def calc_mean_without_outlier(self):

        self.mean_without_outlier = round(self.data_frame_timestamp_without_outliers['Timestamps'].mean(), 4)
        #print('Mean without outlier: {}'.format(self.mean_with_outlier))

        return self.mean_without_outlier

    # Return the employees column of the data frame created excluding the outliers
    def return_employees_column_without_outlier(self):

        return self.employees_column_without_outliers


# Main operation
if __name__ == '__main__':

    # print('# _______________________________________________________________________________ #')
    # print('#                                                                                 #')
    # print('# [ CIDC Challenge - Building a graphic report trough a spread sheet ]            #')
    # print('#                                                                                 #')
    # print('# -> Pedro Lopes de Oliveira - Undergraduated Telecommunications Engineer         #')
    # print('# -> Yara Caroline Tavares Mendes - Undergraduated Telecommunications Engineer    #')
    # print('#                                                                                 #')
    # print('# _______________________________________________________________________________ #')
    # print('#                                                                                 #')
    #
    # os.system('PAUSE')
    # os.system('cls')

    # archive_name = input('Archive name (without extension and on the same folder): ')
    archive_name = 'report-task-log-report-202002071126'

    # Instance of Info class, will give us the basic infos
    information = Info(archive_name)
    information.show_basic_info()

    # Calculus of the number informations englobing operators and services
    information.calc_number_info_operators()
    information.calc_number_info_services()

    # Instance of spreadsheet, will transform the spreadsheet for better execution of operations
    spreadsheet = Spreadsheet(archive_name)
    spreadsheet.timestamp_conversion()
    spreadsheet.timestamp_designation()

    # Calculus of std deviation and mean, considering outliers
    standard_deviation_with_outlier = spreadsheet.calc_std_deviation_with_outlier()
    mean_with_outlier = spreadsheet.calc_mean_with_outlier()

    # Receive the outlier exclusion pattern, on the case 3 times the standard deviation
    # outlier_pattern = int(input('Outlier exclusion pattern (times standard deviation): '))
    outlier_pattern = 3

    outlier_pattern_times = outlier_pattern * standard_deviation_with_outlier
    outlier_pattern_split = standard_deviation_with_outlier / outlier_pattern

    # Exclusion of outliers
    data_frame_employees_without_outlier = spreadsheet.exclude_outliers(outlier_pattern)

    # Calculus of std deviation and mean, desconsidering outliers
    std_deviation_without_outlier = spreadsheet.calc_std_deviation_without_outlier()
    mean_without_outlier = spreadsheet.calc_mean_without_outlier()

    # Calculus of the number informations englobing employees
    timestamps_employees = spreadsheet.timestamp_designation()
    information.calc_number_info_employees_with_outlier(mean_with_outlier, timestamps_employees)
    information.calc_number_info_employees_without_outlier(mean_without_outlier, data_frame_employees_without_outlier)

    # Graphics / Histograms - using matplotlib
    # information.show_graphic_with_outliers(timestamps_employees[1], mean_with_outlier, standard_deviation_with_outlier)
    # information.show_graphic_without_outliers(data_frame_employees_without_outlier['Duration [s]'],
    #                                           mean_without_outlier, std_deviation_without_outlier)

    information.operators_obj.count_number_of_services_without_outlier(data_frame_employees_without_outlier)
    information.operators_obj.count_number_of_unique_services_per_operator_without_outlier(data_frame_employees_without_outlier)
    information.services_obj.count_number_of_unique_services_without_outlier(data_frame_employees_without_outlier)

    # Mean informations for each class - inside the class Info we use it's objects to call the respective function
    information.services_obj.calc_services_mean_duration(data_frame_employees_without_outlier)
    information.employees_obj.calc_mean_duration_per_employee(data_frame_employees_without_outlier)
    information.operators_obj.calc_operators_mean_duration(data_frame_employees_without_outlier)

    information.show_graphic_employees_mean(information.employees_obj.employees_mean, mean_without_outlier, std_deviation_without_outlier)
    # information.show_graphic_operators(information.operators_obj.number_of_services, 'considering outliers')
    # information.show_graphic_operators_unique_services(information.operators_obj.count_number_of_unique_services_per_operator(), 'considering outliers')
    # information.show_graphic_operators_mean(information.operators_obj.calc_operators_mean_duration(data_frame_employees_without_outlier), 'considering outliers')

    #os.system('PAUSE')

