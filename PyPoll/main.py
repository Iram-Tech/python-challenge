import pandas as pd

location = "Resources/election_data.csv"

election_data_df = pd.read_csv(location)

# Loading all unique counties
unique_counties = election_data_df['County'].unique()

# Loading unique candidates
unique_candidates = election_data_df['Candidate'].unique()

# Total number of voters
total_votes = len(election_data_df['Voter ID'])

#Dictionary created to load data from each county
loaded_data = {
	
}
# Creating a txt file to load results
load_poll_results = open('Analysis/poll_results.txt', 'w')

# Loads all unique votes from every county (Made accidentally)
def get_county_vote( x ):
	return len([ county for county in election_data_df['County'] if x in county ])

# Loads all percentage of votes from every county (Made accidentally)
def get_county_percentage( county, all_vote_count ):
	return round( county / all_vote_count * 100,2 )

# Loads total votes from every candidate
def get_candidate_vote( x ):
	return len([ candidate for candidate in election_data_df['Candidate'] if x in candidate ])

# Loads percentage of votes from every candidate
def get_candidate_percentage( county, all_vote_count ):
	return round( county / all_vote_count * 100, 2)

# Loop through every candidate
for i in unique_candidates:
	# Save the candidate, the candidate's total votes, and the percentage of votes for the candate to the Loaded_Data dictionary
	loaded_data[i] = [get_candidate_vote( i ), get_candidate_percentage( get_candidate_vote( i ), total_votes )]

# Print election results and save them to a .txt file in the Analysis directory
def print_election_results(candidate_data):
	# Compare is going to store the highest number of votes and compare it with every candidate
	compare = 0

	# Print the total number of votes in a way that's easy to see
	print('\n\n')
	print('Election Results')
	print('-------------------------')
	print(f"The total number of votes is: {total_votes}")
	print('-------------------------')

	# Loop through all candidates in the loaded_data dictionary
	for x in loaded_data:
		# Print the candidate and their election results to the screen
		print(f"{x}: {candidate_data[x][1]}% ({candidate_data[x][0]})")

		# If the candidate has more votes than the number in the compare variable
		if candidate_data[x][0] > compare:
			# Assign the total number of votes to the compare variable and set the winner to the candidate
			compare = candidate_data[x][0]
			winner = x

	# Print the winner to the screen
	print('-------------------------')
	print(f'Winner: {winner}')
	print('-------------------------\n')

	# Save O'Tooley's results to a variable so that we can print his results to the screen
	# and save his results in a .txt file.
	tooley_percentage_of_votes = loaded_data["O'Tooley"][1]
	tooley_total_votes = loaded_data["O'Tooley"][0]

	# Save the results in the poll_results.txt file
	load_poll_results.write(
		f'Election Results\n'
		f'-------------------------\n'
		f'The total number of votes is: {total_votes}\n'
		f'Khan: {loaded_data["Khan"][1]}% ({loaded_data["Khan"][0]})\n'
		f'Correy: {loaded_data["Correy"][1]}% ({loaded_data["Correy"][0]})\n'
		f'Li: {loaded_data["Li"][1]}% ({loaded_data["Li"][0]})\n'
		f"O'Tooley: {tooley_percentage_of_votes}% ({tooley_total_votes})\n"
		f'-------------------------\n'
		f'Winner: {winner}\n'
		f'-------------------------'
		)


# This is code that I started with but I decided to improve my code with functions
# to improve flexibility
election_data_dictionary = {
	'Total-Votes': len(election_data_df['Voter ID']),
	'Marsh': len([ county for county in election_data_df['County'] if 'Marsh' in county ]),
	'Queen': len([ county for county in election_data_df['County'] if 'Queen' in county ]),
	'Bamoo': len([ county for county in election_data_df['County'] if 'Bamoo' in county ]),
	'Trandee': len([ county for county in election_data_df['County'] if 'Trandee' in county ]),
	'Raffah': len([ county for county in election_data_df['County'] if 'Raffah' in county ])
}

# This is code that I started with but I decided to improve my code with functions
# to improve flexibility
Marsh_Votes = round( election_data_dictionary['Marsh'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Queen_Votes = round( election_data_dictionary['Queen'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Bamoo_Votes = round( election_data_dictionary['Bamoo'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Trandee_Votes = round( election_data_dictionary['Trandee'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Raffah_Votes = round( election_data_dictionary['Raffah'] / election_data_dictionary['Total-Votes'], 2 ) * 100

# Run election results function. Results will be printed in the console and 
# saved to the poll_results.txt file within the Analysis directory
print_election_results(loaded_data)
