#print("Hello world")

#print("hello")

counties=["Arapahoe","Denver","Jeffreson"]
if counties[1]== "Denver": 
    print(counties[1])

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)
    
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county] )

for county in  counties_dict:
    print(counties_dict.get(county))


for county,voters in counties_dict.items():
    print(county,voters)

#Skill drill -Print each county and registered voter form the counties 
#                   dictionary so that the output looks like this:
                   #Arapahoe  county has 422829 registered voters
                   #Denver  county has 463353 registered voters
                   #Jefferson  county has 432438 registered voters
for county,voters in counties_dict.items():
   print(county, " county has" , (voters),"registered voters")



voting_data= [{"county":"Arapahoe","registerd voters":422829},
               {"County":"Denver","registered voters":463533},
               {"county":"Jefferson","registered voters":432438} ]
for county_dict in voting_data:
    print(county_dict)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for i in range(len(voting_data)):

      print(voting_data[i]['county'])

for county_dict in voting_data:      
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:  

     print(county_dict.values())


for county_dict in voting_data:    

   for value in county_dict:      

       print(value)

#How would you retrieve the number of registered voters from each dictionary?
for county_dict in voting_data:

     print(county_dict['registered_voters'])     



for county_dict in voting_data:

     for key, value in county_dict.items():

         print(value)    


#If we only want to print the county name from each dictionary, we can use county_dict['county'] in the print statement for the for loop.

for county_dict in voting_data:
    print(county_dict['county'])

#To see an example, let's edit the code we wrote to calculate the percentage of votes using f-string literals.
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#And here's how you would edit the code to use f-strings.
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Multiple f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes"
    f"The total number of votes in the election was {total_votes}"
    f"You received {candidate_votes/total_votes *100}:% of the total votes")
print(message_to_candidate)
     
#Skill drill Refer to the following dictionary to complete the activity.
#Print each county and registered voter from the dictionary. The output should look like the following:


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registred voters")

#for i in voting_data:
    #print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")
#
#Arapahoe county has 422,829 registered voters.
#Denver county has 463,353 registered voters.
#Jefferson county has 432,438 registered voters.    




#3.2.11
#Refer to the following dictionary to complete the activity.
#Print each county and registered voter from the dictionary. The output should look like the following:

#voting_data = [f'{"co345unty":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}"']
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")