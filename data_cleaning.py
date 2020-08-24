#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 2020

@author: Josh Fuchs

Quick program to read in some fake patient health data and do basic cleaning
"""


import pandas as pd

#read in fake patient data
patient_data = pd.read_csv('fake_patients.csv')


#Rename two of the column headings
patient_data = patient_data.rename(columns={'PID': 'patient_id','DOB':'date_of_birth'})


#For all column headings, convert to lowercase and replace space with _
patient_data.columns = pd.Series(patient_data.columns).str.lower()
patient_data.columns = pd.Series(patient_data.columns).str.replace(' ','_')


#For all values in the gender column, turn to lowercase
patient_data['gender'] = patient_data['gender'].str.lower()

#Create a new column for Full Names
full_names = [patient_data['first_name'][x] + ' ' + patient_data['last_name'][x] \
              for x in range(0,len(patient_data['first_name']))]
patient_data['full_name'] = full_names

#Change the formatting of the date of birth to mm/dd/yyyy
for x in range(0,len(patient_data['date_of_birth'])):
    patient_data['date_of_birth'][x] = patient_data['date_of_birth'][x][5:7] + '/' + \
        patient_data['date_of_birth'][x][8:10] + '/' + patient_data['date_of_birth'][x][0:4]

#Split the address column into address_street, address_city, address_state, address_zip

#Save to CSV
#patient_data.to_csv('updated_patient_data.csv',index=False)









