import pandas as pd

location = "Resources/election_data.csv"

election_data_df = pd.read_csv(location)
unique_counties = election_data_df['County'].unique()
total_votes = len(election_data_df['Voter ID'])
loaded_data = {
	
}
load_poll_results = open('Analysis/poll_results.txt', 'w')

def get_county_vote( x ):
	return len([ county for county in election_data_df['County'] if x in county ])

def get_county_percentage( county, all_vote_count ):
	return round( county / all_vote_count, 2 ) * 100

for i in unique_counties:
	loaded_data[i] = [get_county_vote( i ), get_county_percentage( get_county_vote( i ), total_votes )]
	print(get_county_vote( i ))

def print_election_results(county_data):
	for x in loaded_data:
		print(f"{x}: {county_data[x][1]}% ({county_data[x][0]})")


election_data_dictionary = {
	'Total-Votes': len(election_data_df['Voter ID']),
	'Marsh': len([ county for county in election_data_df['County'] if 'Marsh' in county ]),
	'Queen': len([ county for county in election_data_df['County'] if 'Queen' in county ]),
	'Bamoo': len([ county for county in election_data_df['County'] if 'Bamoo' in county ]),
	'Trandee': len([ county for county in election_data_df['County'] if 'Trandee' in county ]),
	'Raffah': len([ county for county in election_data_df['County'] if 'Raffah' in county ])
}

Marsh_Votes = round( election_data_dictionary['Marsh'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Queen_Votes = round( election_data_dictionary['Queen'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Bamoo_Votes = round( election_data_dictionary['Bamoo'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Trandee_Votes = round( election_data_dictionary['Trandee'] / election_data_dictionary['Total-Votes'], 2 ) * 100
Raffah_Votes = round( election_data_dictionary['Raffah'] / election_data_dictionary['Total-Votes'], 2 ) * 100


print('\n\n')
print('Election Results')
print('-------------------------')
print(f"The total number of votes is: {total_votes}")
print('-------------------------')
print_election_results(loaded_data)
load_poll_results.write(
	f'Election Results\n'
	f'-------------------------\n'
	f'The total number of votes is: {total_votes}\n'
	f'-------------------------\n'
	f'Marsh: {Marsh_Votes}% ({election_data_dictionary["Marsh"]})\n'
	f'Queen: {Queen_Votes}% ({election_data_dictionary["Queen"]})\n'
	f'Bamoo: {Bamoo_Votes}% ({election_data_dictionary["Bamoo"]})\n'
	f'Trandee: {Trandee_Votes}% ({election_data_dictionary["Trandee"]})\n'
	f'Raffah: {Raffah_Votes}% ({election_data_dictionary["Raffah"]})\n'
	)