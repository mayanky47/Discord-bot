import requests
import pandas as pd

API_KEY = '25BAF7B524530164FDBCAC4C9B1F990F'

STEAM_ID = 'Mayanky47'

MATCHES_REQUESTED = 20


API_URL = f'http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?key={API_KEY}&account_id={STEAM_ID}&matches_requested={MATCHES_REQUESTED}'
response = requests.get(API_URL)

if response.status_code == 200:
	print("helo")
	# data = response.json()
	data = response.json()['result']['matches']

	df = pd.DataFrame(data)
	df.to_csv('your_file.csv', index=True)
	if 'radiant_win' in df and 'player_slot' in df:
		# Filter matches where the player is on the radiant team and check for a win
		radiant_wins = df[df['player_slot'] < 128]['radiant_win'].sum()
		radiant_losses = MATCHES_REQUESTED - radiant_wins

		print(f'Radiant Wins: {radiant_wins}, Radiant Losses: {radiant_losses}')


else:
	print("API request failed.")

column_labels = df.columns

print("Column Labels:")
for label in column_labels:
	print(label)

print(df['match_seq_num'])