# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:27:30 2022
@author: sebastian Ramirez
student id=11736865

"""
import matplotlib.pyplot as plt
import csv #Call the CSV library
import sys




def main():
    #call the file and stored structure dictionary
    country_dict = file()
    #call main problem
    menu(country_dict)
def menu(country_dict):
    
    # do while user = 5 exception input handeling
    while True:
        # print menu
        
        print('--------------------------------------')
        print('Main Menu CO-2 Emissions Data Explorer')
        print('--------------------------------------')
        print("(1) CO2 emissions breakdown")
        print("(2) Maximum emissions per GDP")
        print("(3) Top 10 GHG countries")
        print("(4) Energy consumption distribution")
        print("(5) Exit")
        try:
            # input user
            user_option = int(input('Enter your choice: '))
            #error handle
        except ValueError:
            print ('Invalid input!!. Enter an option between 1-5.')
            continue
        
        if not user_option in range(1, 6):
            print ('Invalid input. Enter a value between 1-5.')
            continue
        # entry case
        if (user_option == 1):# option1
            cotwo_break(country_dict)# call function
            
        if (user_option == 2):# option2
            max_emission(country_dict)# call function
            
        if (user_option == 3):# option3
            top_ghg(country_dict)# call function
        
        if (user_option == 4):# option4
            energy_consu(country_dict)# call function
            
        if (user_option == 5): # Exit 
            print ('Thanks for exploring the CO2 Emissions Data Base')
            break
    
def cotwo_break(country_dict):
    # prompt user and check if the imput exists in the database
    country = check_dataBase(country_dict)
    list_values = []
    list_labels = []
    
    # header for look up and print results
    header = ['Coal','Cement','Flaring',
              'Gas','Oil','Other Industry']
    
    print("\n++++++<" + country + ">++++++\n")
    print(country + " CO2 emissions breakdown:\n")
    #
    
    
    #print the breackdown to find the percapital of each emission is divided
    #its total emissions by its population and multiply by 1e+9 to pass kg
    for i in range(0,6):
        # avoid empty columms
        if (country_dict[country][header[i]]== ''):
            continue
        else:
            # print and the breakdown
            print(header[i],': ', 
                  format((float(country_dict[country][header[i]])/
                          float(country_dict[country]['Population']))*1e+9,',.2f')
                  )
            #storage in a list structure to use them to plot
            list_values += [(float(country_dict[country][header[i]])/
                             float(country_dict[country]['Population']))*1e+9]
            list_labels += [header[i]]
    
    
    # look up total CO2 / population     
    total = (float(country_dict[country]['CO2'])/
             float(country_dict[country]['Population']))*1e+9
                  
    
    #print total
    print('*******************************') 
    print('Total: ' + str(format(total,',.2f')) +  ' kg per person')
    
    # Pie chart: provide two lists for values and labels
   
    
    plt.pie(list_values,labels=list_labels,wedgeprops = {"edgecolor":'black'},
            autopct='%1.1f%%', shadow = True, startangle=90,
            textprops = dict(color ="black"))
    plt.title(country + ' CO2 emissions breakdown', fontsize=18)
    plt.tight_layout()
    plt.show()
    
    
def max_emission(country_dict):
    
    
    #initialize dictionary
    total = {}
    # calculate the  total-GHG (greenhouse gas) emissions per dollar of GDP.
    for row in country_dict:
        total[row] = (float(country_dict[row]['Total GHG'])/
                      float(country_dict[row]['GDP']))*1e+9
    """ 
    # I can sorted or go directly to the max number with the method 
    # below key=lambda x: x[1] it is A sorting mechanism that allows
    us to sort our dictionary by value. This is an example
    of a Lambda function, which is a function without a name
    """
    # find the highest number using max method
    total_max = max(total.items(), key=lambda x: x[1])
    
    #print result
    print(total_max[0] + ' had the maximum greenhouse gas emissions: ' +
          str(format(total_max[1], ',.2f')) +' kg per dollar of GDP') 
    #print(total_ghg)
            

    
    

def top_ghg(country_dict):
    #Submenu 
    while True:
        
        print('--------------------------------------')
        print('------Choose The Greenhouse Gas-------')
        print('--------------------------------------')
        print("(1) Methane")
        print("(2) Nitrous Oxide")
        print("(3) Total")
        print("(4) Back Main Menu")
        try:
            #input  handle exception 
            user_option = int(input('Enter your choice: '))
        except ValueError:
            print ('Invalid input!!. Enter an option between 1-4.')
            continue
        
        if not user_option in range(1, 5):
            print ('Invalid input. Enter a value between 1-4 .')
            continue
        #case menu
        if (user_option == 1):
            trend('Methane',country_dict)
            
        if (user_option == 2):
            trend('Nitrous Oxide', country_dict)
            
        if (user_option == 3):
            trend('Total GHG', country_dict)
        
        if (user_option == 4):# exit submenu
            break
            
            
def trend(dataBaseLabel, country_dict):
    
    # lists to keep values and labels 
    list_values = []
    list_labels = []
    
    topten = {}
    
    for row in country_dict:
        topten[row] = (round(float(country_dict[row][dataBaseLabel])/
                             float(country_dict[row]['Population'])*1e+6, 2))
    # print(topten)
    
    sorted_topten = sorted(topten.items(), key=lambda x: x[1])
    
   
    
    # list_values ans List labels
    """
    when it is sorted the dictionary, it convert into tuples every 
    pair this bring errors to convert into the list to plot the results 
    """
    #storage top ten list of labels and values
    for line in range(len(sorted_topten)-10,len(sorted_topten)):
            
            list_values += [sorted_topten[line][1]]
            list_labels += [sorted_topten[line][0]]
    
    
    #print(list_labels)
    #function to print the values on the top of corresponding bar
    def add_value_label(x_list,y_list):
        for i in range(1, len(x_list)+1):
            plt.text(i-1,y_list[i-1],y_list[i-1],ha="center")
            
    #plot bar chart        
    plt.title(dataBaseLabel + ' CO2 emissions breakdown', fontsize=18)
    plt.xticks(rotation=30, ha='right')# make readable labels
    plt.ylabel(dataBaseLabel + '(Tonnes per year)')# y label
    add_value_label(list_labels,list_values)# plot values text
    plt.bar(list_labels, list_values)
    plt.show()
    
        
    
def energy_consu(country_dict):
    # list to plot with box just require list values
    list_values = []
    
    for row in country_dict:
            list_values += [(float(country_dict[row]['Energy Consumption'])/
                             float(country_dict[row]['Population']))*1e+6]
    
    #Plot box chart
    plt.boxplot(list_values)
    plt.ylabel('KiloWatt-hours')
    plt.show()
    
def check_dataBase(country_dict):
    # initialize string 
    
    while True:
        
        try:
            # input file name
            country = input('Please enter the country name: ').title()
            space_split = country.split() # ["item1", "item2,", "item3"]
         
            # process input reduce input error " "
            # print comparable words
            entry = ''
            for item in range(len(space_split)):
                entry += space_split[item]
                if item < len(space_split)-1:
                    entry += ' '
                else:
                    break
        
            #look up the word at the dictionary exception if not found
            country_dict[entry]
            return entry
        except:
            print('That is an invalid or unknown country.')    



        
    

def file(): 
    
    def readerror():
        print('File not processed')
        sys.exit()  
        
    # print title
    print('------------------------------')
    print('CO-2 Emissions Data Explorer')
    print('------------------------------')
    
   
    #handle Incorrect database file names 
    while True:    
        
        try:
            file_name = str(input("Enter File name/type 'e' for exit -> "))
            
            if file_name == 'e':
                print("Exit")
                break
            
            #open the file
            file = open(file_name,'r') 
            
            #read the file .csv        
            carbon = csv.reader(file)
            #Create empty dictionaryto populate 
            reader = {}
            
            #jump the header
            next(carbon)
            
            #carbon.readline()
            
            #Read the File and create loop to pass the data into the dictionary
            #The contry name is my key to access to the data create a subdictionary 
            #incide to the other main dictionary
            
            #row[0] = key (country name) .title() 
            #convert country title form reduce error when look up input user
            print('Loading......')
            for row in carbon:
                
                if row[0] == '' or row[0] == 0 :
                    #raise ValueError('No data available File must not use')
                    print('keys no found, file must be not used')
                    readerror()
                   
                else:                    
                    reader[row[0].title()] = {'CO2':row[1],	'Coal':row[2],
                                              'Cement':row[3],	'Flaring':row[4],	
                                              'Gas':row[5],	'Oil':row[6],
                                              'Other Industry':row[7],	'Total GHG':row[8],
                                              'Methane':row[9],	'Nitrous Oxide':row[10],
                                              'Population':row[11], 'GDP':row[12],
                                              'Energy Consumption':row[13]}
                # check if the values that can be use as divisors or are # raise exception if not 
                1/float(row[11])+1/float(row[12])+1/float(row[11])
            break 
        except OSError:
            print('File not found try again')
        except ZeroDivisionError:
            print('Population/GDP/Energy Consumption can not divide by zero')
        
        except ValueError:
            print('error some values could not convert string to float - '+
                  'please check enter correct file')
        except:
             print('File empty or file problems please check enter correct file')
        
       
    if file_name == 'e':
        readerror()
      
    #close the file 
    file.close() 
    #return dictionary
    print('File load!!')
    return reader
        
  

main()