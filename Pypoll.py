# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote

import datetime as dt
now=dt.datetime.now()
print("The right time is",now)
import os
import csv
file1_to_load=os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.text")
with open(file1_to_load) as election_data:
#    print(election_data)

#file1_to_save = os.path.join("Analysis","election_analysis.text")
#open(file1_to_save,"w")
#outfile=open(file1_to_save,"w")
##outfile.write("Hello World")
#outfile.close()


# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("Analysis","election_analysis.text")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("-------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Denver , ")\n
    #txt_file.write("Jefferson , ")

# To do: read and analyze the data here
    file_reader = csv.reader(election_data)

#print each row in csv format
    #for row in file_reader:
        #print(row)
    headers = next(file_reader) 
    print(headers)

    # Read and print the header row.
         

