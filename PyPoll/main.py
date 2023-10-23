import os
import csv

# Set file path
poll_path = os.path.join("PyPoll", "Resources", "election_data.csv")

# Store the name of each candidate from each individual poll
raw_votes = []

#-----------------------Read CSV file and append all raw votes to raw_votes list------------------

# Open data
with open(poll_path, mode= "r", encoding="UTF-8") as csvfile:
    poll_data = csv.reader(csvfile, delimiter=",")

    # Skip headers
    next(poll_data, None)

    # Put data from CSV in list
    for row in poll_data:
        raw_votes.append(row[2])

#-----------------------Use for loop to gather all necessary data-------------------------------

# Variables to store data
total_votes = len(raw_votes)
candidates = []

# Use for loop to store every unique name into candidates list
for candidate in raw_votes:
    if candidate not in candidates:
        candidates.append(candidate)


# Variables to store data
candidate_vote_count = []
candidate_vote_percentage = []
max_votes = 0
winner = ""
formatted_results = ""

# Use another for loop to go through each index of candidates list
for x in range(len(candidates)):

    # Count how many votes each candidate received by counting how many times their name occur in raw_votes list. Append count to list.
    candidate_vote_count.append(raw_votes.count(candidates[x]))

    # Calculate each candidate vote percentage by dividing each candidate vote count by total votes * 100. Append percentage to list.
    candidate_vote_percentage.append(round(candidate_vote_count[x]/total_votes * 100, 3))

    # Use if statement to find the candidate with the most votes. Store name in winner variable
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        winner = candidates[x]

    # Format the results of every candidate that will be used later in our text file
    formatted_results += f"{candidates[x]}: {candidate_vote_percentage[x]}% ({candidate_vote_count[x]})\n\n"

#-----------------------Format final analysis text---------------------------------------------

# Create three seperate variables to store data needed for final text
text_1 = (f"Election Results \n\n---------------------- \n \nTotal Votes: {total_votes}" 
f"\n\n---------------------- \n\n")
text_2 = formatted_results
text_3 = (f"---------------------- \n\nWinner: {winner}\n\n---------------------- \n")

# Concat all text variables in order to create final text
final_analysis_text = text_1 + text_2 + text_3

#---------------------Write final analysis to text file-------------------------------------------

# Set file path
analysis_txt_file = os.path.join("PyPoll", "Analysis", "poll_analysis.txt")

# Write to file
with open(analysis_txt_file, mode= "w", encoding="UTF-8") as text:
    text.write(final_analysis_text)

#-------------------------------Print to terminal------------------------------------------------

print(final_analysis_text)
