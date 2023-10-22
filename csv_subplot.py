import csv              #import necessary libraries like csv, pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

def new_csv():# Function to create a new csv file(output.csv) by taking inputs from input.csv file
    skip_row = 9     # This variable will be used to skip the initial unwanted rows in the input.csv file
    new_1 = list()

    with open('input.csv',"r", newline = '') as csvfile_1, open('output.csv', 'w', newline = '') as csvfile_2:
        """
        Opening the input.csv file for the purpose of reading data from it and also creating a new file named 
        output.csv to write into it
        
        """
        csv_reader = csv.reader(csvfile_1, delimiter = ';')  
        rows = list(csv_reader)
        
        for item_1, item_2 in zip(rows[6], rows[7]): # Loop to exatract the sensornames and units from the rows
            new_1.append(f"{item_1}_[{item_2}]")
        
        csv_writer = csv.writer(csvfile_2, delimiter = ';')
        csv_writer.writerow(new_1)
        with open('input.csv', "r", newline='') as csvfile_1:
            csv_reader = csv.reader(csvfile_1, delimiter = ';')
            
            for _ in range(skip_row): # Loop to skip the pointer to the desired location
                next(csv_reader,None)
                
            for row in csv_reader: # Loop to write into the output.csv file
                csv_writer.writerow(row)
    

def subplot(): # Function to create subplot
    data = pd.read_csv("output.csv", sep =';')  # Read data from output.csv file using pandas framework
    columns_to_plot = ["Omega_[rpm]", "MSTor_[deg]" , "Pi1_[deg]"] 
    """
    The names of columns whose graphs will be plotted 
    and the columns can be changed for the convenience of the user
    """
    num_plots = len(columns_to_plot)
    fig, axs = plt.subplots(num_plots, 1, figsize=(8, 4 * num_plots))
    x_axis_para = "t_[(s)]" # Considering Time as the x axis parameter
    data[x_axis_para] = data[x_axis_para].str.replace(',', '.').astype(float) # Converting datas from string data types to float

    subplot_colors = ['b', 'g', 'r', 'c', 'm'] 

    subsample_rate = 20
    subsampled_data_x = data[x_axis_para][::subsample_rate]
    """
    Subsampling of the data is done so as to make the graph look nice and not crowded. 
    Every 20 th element from the column will be considered for plotting graph. This also can be changed by the user 
    """
    for i, column in enumerate(columns_to_plot): # Iterate through the columns and create subplots

        data[column] = data[column].str.replace(',', '.').astype(float)
        subsampled_data_y = data[column][::subsample_rate]

        axs[i].plot(subsampled_data_x, subsampled_data_y, label = column, color=subplot_colors[i])  
        axs[i].set_title(f"Plot of {x_axis_para} v/s {column}")
        axs[i].set_xlabel(f"{x_axis_para}")
        axs[i].set_ylabel(f"{column}")
        axs[i].legend()

    plt.tight_layout()   
    plt.savefig('*.eps', format='eps', bbox_inches='tight') # This saves the subplot in the directory
    plt.show()






            
 
        
              
               
         
