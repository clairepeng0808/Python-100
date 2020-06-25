#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Doctor Scheduler** - Create a patient class and a doctor class.
Have a doctor that can handle multiple patients and setup a
scheduling program where a doctor can only handle 16 patients
during an 8 hr work day.
'''

from datetime import datetime
from collections import defaultdict


class Doctor:

    doctor_list = []

    def __init__(self, name):
        self.schedule = defaultdict(list)  # {date:patient}
        Doctor.doctor_list.append(name)

    def appointment(self, date, patient_name):
        self.schedule[date].append(patient_name)


class Patient:
    def __init__(self, name):
        self.name = name


def input_date():

    while True:

        try:
            date_string = input(
                '\n\nPlease enter the date you would like to make an appointment on (yyyy-mm-dd): ')
            date = datetime.strptime(date_string, '%Y-%m-%d').date()

            if date < date.today():
                print('Please enter a future date.')

            else:
                return date_string

        except ValueError:
            print('Wrong date format.')


def input_doctor_name():

    while True:
        doctor_name = input('\n\nWhich doctor would you like to make an appointment with? '
                            'Claire, Tony, Bagel: ').capitalize()

        if doctor_name in Doctor.doctor_list:
            return doctor_name

        else:
            print(f'No doctor named {doctor_name}')


def input_patient_name():
    patient_name = input('\n\nPlease enter your name: ')
    return patient_name


Claire = Doctor('Claire')
Tony = Doctor('Tony')
Bagel = Doctor('Bagel')

doctors = {
    'Claire': Claire,
    'Tony': Tony,
    'Bagel': Bagel
}


if __name__ == '__main__':

    while True:

        patient = input_patient_name()
        doctor = doctors[input_doctor_name()]

        while True:

            date = input_date()
            doctor.appointment(date, patient)
            appointments = len(doctor.schedule.get(date, 0))

            if appointments < 16:
                print('Your appointment is done!')
                break

            else:
                print('No available time slot for the day. Please pick another day.')
