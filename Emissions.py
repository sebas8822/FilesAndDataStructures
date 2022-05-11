# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:27:30 2022

@author: sebas
"""
import matplotlib.pyplot as plt
import csv#Call the CSV library

def main():
    
    country_dict = file('carbon.csv')
    
    
    menu(country_dict)





def menu(country_dict):
    
    while True:
    
        print('--------------------------------------')
        print('Main Menu CO-2 Emissions Data Explorer')
        print('--------------------------------------')
        print("(1) CO2 emissions breakdown")
        print("(2) Maximum emissions per GDP")
        print("(3) Top 10 GHG countries")
        print("(4) Energy consumption distribution")
        print("(5) Exit")
        try:
            
            user_option = int(input('Enter your choice: '))
        except ValueError:
            print ('Invalid input!!. Enter an option between 1-5.')
            continue
        
        if not user_option in range(1, 6):
            print ('Invalid input. Enter a value between 1-5 .')
            continue
        
        if (user_option == 1):
            cotwo_break(country_dict)
            
        if (user_option == 2):
            max_emission(country_dict)
            
        if (user_option == 3):
            top_ghg(country_dict)
        
        if (user_option == 4):
            energy_consu(country_dict)
            
        if (user_option == 5):
            print ('Thanks for exploring the CO2 Emissions Data Base')
            break
    
def cotwo_break(country_dict):
    # prompt user and check if the imput exists in the database
    country = check_dataBase(country_dict)
    list_values = []
    list_labels = []
    result = 0
    
    header = ['coal_co2','cement_co2','flaring_co2',
              'gas_co2','oil_co2','other_industry_co2']
    
    print("\n++++++" + country + "++++++\n")
    print(country + " CO2 emissions breakdown:")
    #
    
    
    #print the breackdown 
    for i in range(0,6):
        if (country_dict[country][header[i]]== ''):
            continue
        else:
            print(header[i],': ', country_dict[country][header[i]] )
            list_values += [float(country_dict[country][header[i]])]
            list_labels += [header[i]]
    for val in list_values:
        result = result + val
    
    #print(list_values)
    
    print('*******************************') 
    print('Total: ' + str(result) +  ' kg per person')
    
    # Pie chart: provide two lists for values and labels
    # normalize option is needed when values do not add up to 1
    
    plt.pie(list_values,labels=list_labels,wedgeprops = {"edgecolor":'black'})
    plt.title(country + ' CO2 emissions breakdown')
    plt.tight_layout()
    plt.show()
    
    
def max_emission(country_dict):

    total_ghg = {}
    
    for row in country_dict:
        total_ghg[row] = (float(country_dict[row]['total_ghg']))
    """ 
    # I can sorted or go directly to the max number with the method 
    # below key=lambda x: x[1] it is A sorting mechanism that allows
    us to sort our dictionary by value. This is an example
    of a Lambda function, which is a function without a name
    """
    total_ghg = max(total_ghg.items(), key=lambda x: x[1])

    print(total_ghg[0] + ' had the maximum greenhouse gas emissions:' +
          str(total_ghg[1]) +' kg per dollar of GDP') 
    #print(total_ghg)
            

    
    

def top_ghg(country_dict):
    while True:
        
        print('--------------------------------------')
        print('------Choose The Greenhouse Gas-------')
        print('--------------------------------------')
        print("(1) Methane")
        print("(2) Nitrous Oxide")
        print("(3) Total")
        print("(4) Back Main Menu")
        try:
            
            user_option = int(input('Enter your choice: '))
        except ValueError:
            print ('Invalid input!!. Enter an option between 1-4.')
            continue
        
        if not user_option in range(1, 5):
            print ('Invalid input. Enter a value between 1-4 .')
            continue
        
        if (user_option == 1):
            trend('methane',country_dict)
            
        if (user_option == 2):
            trend('nitrous_oxide', country_dict)
            
        if (user_option == 3):
            trend('total_ghg', country_dict)
        
        if (user_option == 4):
            break
            
            
def trend(dataBaseLabel, country_dict):
    
     
    list_values = []
    list_labels = []
    
    topten = {}
    
    for row in country_dict:
        topten[row] = (float(country_dict[row][dataBaseLabel]))
    # print(topten)
    
    sorted_topten = sorted(topten.items(), key=lambda x: x[1])
    
    print(sorted_topten[0][0])
    print(type(sorted_topten[0][0]))
    
    # list_values
    """
    when it is sorted the dictionary, it convert into tuples every 
    pair this bring errors to convert into the list to plot the results 
    """
    for line in range(len(sorted_topten)-10,len(sorted_topten)):
            
            list_values += [sorted_topten[line][1]]
            list_labels += [sorted_topten[line][0]]
    
    print(list_values)
    print(list_labels)
    plt.bar(list_labels, list_values)
    plt.show()
    
        
    
def energy_consu(country_dict):
    list_values = []
    
    for line in country_dict:
            
            list_values += [(float(country_dict[line]['energy_consumption'])/100)]
    
    
    
    print(list_values)
    plt.boxplot(list_values)
    plt.ylim(0,30)
    plt.show()
    
def check_dataBase(country_dict):

    while True:
        
        try:
            country = input('Please enter the country name:').title()
            country_dict[country]
            return country
        except:
            print('that country is not in the database try again')    
        
    

def file(file_name): 
    
    
    print('------------------------------')
    print('CO-2 Emissions Data Explorer')
    print('------------------------------')
    

    
    #handle Incorrect database file names 
    while True:    
        
        try:
            #file_name = input("Enter File name -> ")
            #open the file
            file = open(file_name,'r')
            break
            
        except OSError:
            print('File not found try again')
            
            
            
            
    carbon = csv.reader(file)
    #Create empty dictionary{} to populate 
    reader = {}
    
    #jump the header
    next(carbon)
    
    #Read the File and create loop to pass the data into the list
    #The contry name is my key to access to the data create a dictionary 
    #incide to the other main dictionary
    #row[0] = key 
    for row in carbon:
        reader[row[0]] = {'co2':row[1],	'coal_co2':row[2],
                          'cement_co2':row[3],	'flaring_co2':row[4],	
                          'gas_co2':row[5],	'oil_co2':row[6],
                          'other_industry_co2':row[7],	'total_ghg':row[8],
                          'methane':row[9],	'nitrous_oxide':row[10],
                          'population':row[11], 'gdp':row[12],
                          'energy_consumption':row[13]}
    file.close() 
    return reader
        
    
    
    
    

main()