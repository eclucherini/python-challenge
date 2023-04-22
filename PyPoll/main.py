# Start with necessary imports
import os
import csv

# Use csv path
csvpath = os.path.join("Resources","election_data.csv")
csvpath

# Define variables
candidate_list = []
unique_candidates = []
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

# Open csv file
with open(csvpath) as voter_file:
    csvreader = csv.reader(voter_file,delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

         # Loop through second column to append each row of data to candidates_list (used for unique_candidates list)
        candidate_list.append(row[2])

        # Count the total number of votes cast
        total_votes += 1

        # Calculate number of votes for each candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        else:
            doane_votes += 1

    # print(total_votes)
    # print(stockham_votes)
    # print(degette_votes)
    # print(doane_votes)

# Sort candidate_list alphabetically
sorted_candidate_list = sorted(candidate_list)

# Loop through candidate_list to append the name to unique_candidates list if the following name does not match
for i in range(len(sorted_candidate_list)-1):
    if sorted_candidate_list[i] != sorted_candidate_list[i+1]:
        unique_candidates.append(sorted_candidate_list[i])

# Append the last name to the unique_candidates list (would be excluded with about loop code)
last_candidate = sorted_candidate_list[len(sorted_candidate_list)-1]
unique_candidates.append(last_candidate)

# print(unique_candidates)

# Calculate percentage of votes each candidate won
stockham_votes_percent = stockham_votes/total_votes
degette_votes_percent = degette_votes/total_votes
doane_votes_percent = doane_votes/total_votes

# print(stockham_votes_percent)
# print(degette_votes_percent)
# print(doane_votes_percent)

# Put candidate vote counts into a list
total_votes_by_candidate = [stockham_votes, degette_votes, doane_votes]

# Define new variable based on which of the candidates had the max number of votes
winner_votes = max(total_votes_by_candidate)
winner_name = ""

# Use IF statement to find winner based on max test vote count
if winner_votes == stockham_votes:
    winner_name = "Charles Casper Stockham"
elif winner_votes == degette_votes:
    winner_name = "Diana DeGette"
elif winner_votes == doane_votes:
    winner_name = "Raymon Anthony Doane"
else:
    winner_name = "NO WINNER"

# print(winner_name)

# Create output txt file
output_txt_file = os.path.join("Analysis","analysis.txt")
with open(output_txt_file,"w") as txt_data_file:
    txtwriter = ["Election Results \n",
                 "------------------------- \n",
                 f"Total Votes: {total_votes} \n",
                 "------------------------- \n",
                 f"Charles Casper Stockham: {round(stockham_votes_percent * 100,3)}% ({stockham_votes}) \n",
                 f"Diana DeGette: {round(degette_votes_percent * 100,3)}% ({degette_votes}) \n",
                 f"Raymon Anthony Doane: {round(doane_votes_percent * 100,3)}& ({doane_votes}) \n",
                 "------------------------- \n",
                 f"Winner: {winner_name} \n",
                 "------------------------- \n"]
    txt_data_file.writelines(txtwriter)
    txt_data_file.close()

# Show the output in the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round(stockham_votes_percent * 100,3)}% ({stockham_votes})")
print(f"Diana DeGette: {round(degette_votes_percent * 100,3)}% ({degette_votes})")
print(f"Raymon Anthony Doane: {round(doane_votes_percent * 100,3)}& ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")