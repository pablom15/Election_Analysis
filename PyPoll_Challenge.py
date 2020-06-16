# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Challenge
# 1. Create a list of counties
# 2. Create a dictionary where county is key and votes cast for each county is the value
# 3. Create an empty string that will hold the county with the largest turnout
# 4. Declare a variable that represents the number of votes recieved
# 5. Inside a for loop, add an if statement to check if the county name has already been recorded. Add if not included.
# 6. Use with open() to output results
#   - Create 3 IF statements to print out the voter turnout results
#   - Add the results to output file
#   - print results to terminal

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Challenge: added counties list, dictionary, best county turnout string
county_names = []
counties_votes_dict = {}
best_county_turnout = ''
# Declare a variable that represents the number of votes recieved
highest_county = 0
# Track winning candidate, vote count, and percentage
winning_candidate = ''
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)
    # Read header row.
    headers = next(file_reader)
    # Print each row in the CSV
    for row in file_reader:
        # Add to total votes
        total_votes +=1
        # Get the county and candidate name for each row
        candidate_name = row[2]
        county = row[1]
        #If the candidate does not match any existing candidate add to candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Track the candidates votes
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidates count
        candidate_votes[candidate_name] +=1

        # Challenge: creates a list of counties
        if county not in county_names:
            county_names.append(county)
            # Tracks the counties votes
            counties_votes_dict[county] = 0
        # Add votes to county
        counties_votes_dict[county] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Writes a header for the county results section
    county_header = "County Votes:\n"
    print(county_header)
    txt_file.write(county_header)

    # Challenge: County voting results
    for county in counties_votes_dict:
        # County vote count and percentage
        county_votes = counties_votes_dict[county]
        county_percentage = float(county_votes) / float(total_votes) * 100
        # Print each counties results and writes to txt file
        county_results = (f"{county}: {county_percentage: .1f}% ({county_votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        # Determine the county with the largest turnout
        if county_votes > highest_county:
            highest_county = county_votes
            best_county_turnout = county

    # Print the county with the largest turnout to terminal and write to txt file
    largest_turnout_summary = (
        f"\n----------------------------\n"
        f"Largest County Turnout: {best_county_turnout}\n"
        f"----------------------------\n")
    print(largest_turnout_summary)
    txt_file.write(largest_turnout_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their vote count, and percentage
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage, and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidates results to terminal and txt file
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)