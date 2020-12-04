import requests
import hashlib

# Gera Hash para um determinado password.

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/21BD1/' + query_char 
	res = requests.get(url)
	if res.status_code != 200:
	  raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
	return res


def pwned_api_check(password):
 	print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
 	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

pwned_api_check('123')
