#Dependencies
import csv
import os

#importing the csv file
election_data_csv = os.path.join("Resources","election_data.csv")

#exporting the file
file_to_output = os.path.join("election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidates = []
candidates_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_votes = 0

#Opening the csv file and looping it through

with open(election_data_csv) as election_data:
    reader = csv.reader(election_data)
    
    #skipping the header
    next(reader)
    
    for row in reader:
        total_votes = total_votes + 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_votes[candidate] = 0
        else:
            candidates_votes[candidate] = candidates_votes[candidate] + 1

# Winning Candidate and Vote Count Tracker


with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)


    for candidate in candidates_votes:
        votes = candidates_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes) * 100

        if votes > winning_votes:
            winning_votes = votes
            winning_candidate = candidate
        
        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)