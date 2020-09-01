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

#Split the address column into strret, city, state, and zip
#print(patient_data['address'])
address_street = []
address_city = []
address_state = []
address_zip = []
for x in range(0,len(patient_data['address'])):
    address_zip.append(patient_data['address'][x][-5:])
    address_state.append(patient_data['address'][x][-8:-6])
    street_break = patient_data['address'][x].find('\n')
    city_break = patient_data['address'][x].find(',')
    address_street.append(patient_data['address'][x][0:street_break])
    address_city.append(patient_data['address'][x][street_break+1:city_break])
    
#Add to dataframe and delete old address column
patient_data['address_street'] = address_street
patient_data['address_city'] = address_city
patient_data['address_state'] = address_state
patient_data['address_zip'] = address_zip

patient_data = patient_data.drop(columns='address')

#Reformat the phone numbers to be only 10 digits (area code + number)
print(patient_data['phone_number'][2000:2030])
reformatted_phone = []
for x in range(0,len(patient_data['phone_number'])):
    #First, let's deal with extensions, which all start with 'x'
    extension_break = patient_data['phone_number'][x].find('x')
    if extension_break == -1:
        last = None
    else:
        last = extension_break
    
    #Now we can deal with the beginning of the phone number
    if patient_data['phone_number'][x][0] == '+':
        first = 3
    elif patient_data['phone_number'][x][0] == '0':
        first = 4
    elif patient_data['phone_number'][x][0] == '(':
        first = 1
    else:
        first = 0

    #Do the actual reformatting here
    reformatted_phone.append(patient_data['phone_number'][x][first:last])
    
    #These next two are to ensure formatting is the same
    reformatted_phone[x] = reformatted_phone[x].replace(')','-')
    reformatted_phone[x] = reformatted_phone[x].replace('.','-')

patient_data['phone_number'] = reformatted_phone



#Save to CSV
#patient_data.to_csv('updated_patient_data.csv',index=False)









