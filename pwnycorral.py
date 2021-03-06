# PwnyCorral takes advantage of the HaveIBeenPwned API to determine if an account is compromised.
# The primary goal of this application is to allow organizations/companies to track the breaches
# in which their users have fallen victim.  Identifying accounts which come from one particular
# source may allow proactive remediation.
#
# PwnyCorral's most common flags are -a (add account to DB), -f (add group of accounts to DB), and -g (graph DB to show greatest threat(s)).
#
# Created by Brad Dial:  https://github.com/Radial01

from tinydb import TinyDB, Query, where
import json
import requests
from collections import Counter
import argparse
import time
from operator import itemgetter

Pwny = Query()
db = TinyDB('db.json')
headers = {'User-Agent': 'PwnyCorral'}

def addAccount(accountName, verbose):
	url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + accountName
	response = requests.get(url, headers=headers)

	if (response.status_code) == 404:
		print("The account " + accountName + " has not been breached")
		return;
	json_data = json.loads(response.text)
	dictSize = len(json_data)

	if db.count(where('email') == accountName):
		dupResponse = input("The account " + accountName + " already exists.  Overwrite (Y/n)?  ")
		if dupResponse == 'y':
			db.remove(where('email') == accountName)
			for x in range(dictSize):
				json_data[x]['email'] = accountName
				db.insert(json_data[x])
			print("The account " + accountName + " has been added to the DB")
			if (verbose):
				print(accountDetails(accountName))
		else:
			print("No action taken!")
	else:
		for x in range(dictSize):
			json_data[x]['email'] = accountName
			db.insert(json_data[x])
		print("The account " + accountName + " has been added to the DB")
		if (verbose):
			print(accountDetails(accountName))
	return;

def removeAccount(accountName):
	if db.search(Pwny.email == accountName):
		db.remove(where('email') == accountName)
		print("Email address removed.")
	else:
		print("The email address was not found in your DB.")
	return;

def totalAccounts():
	accTotal = 0
	c = Counter(x['email'] for x in db)
	print(len(set(c)))
	return;

def greatThreat():
	c = Counter(x['Name'] for x in db)
	for k, v in c.items():
		print("{},{}".format(k,v))
	return;

def graphThreat():
	graphData = []

	c = Counter(x['Name'] for x in db)
	for k, v in c.items():
		graphData.append((k,v))
	sortedList = sorted(graphData, key=itemgetter(1), reverse=True)

	max_value = max(count for _, count in sortedList)
	increment = max_value / 25
	longest_label_length = max(len(label) for label, _ in sortedList)

	for label, count in sortedList:
		bar_chunks, remainder = divmod(int(count*8/increment),8)
		bar = '█' * bar_chunks
		if remainder > 0:
			bar += chr(ord('█') + (8 - remainder))
		bar = bar or  '▏'
		print(f'{label.rjust(longest_label_length)} ▏ {count:#4d} {bar}')
	return;

def bulkAccounts(compFile):
	with open(compFile) as f:
		for line in f:
			accountName = line.strip()
			url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + accountName
			response = requests.get(url, headers=headers)
			if (response.status_code) == 200:
				print("The account " + accountName + " was found.")
				json_data = json.loads(response.text)
				dictSize = len(json_data)

				if db.count(where('email') == accountName):
					dupResponse = input("The account " + accountName + " already exists.  Overwrite (Y/n)?  ")
					if dupResponse == 'y':
						db.remove(where('email') == accountName)
						for x in range(dictSize):
							json_data[x]['email'] = accountName
							db.insert(json_data[x])
					else:
						print("No action taken!")
				else:
					for x in range(dictSize):
						json_data[x]['email'] = accountName
						db.insert(json_data[x])
			elif (response.status_code) == 404:
				print("The account " + accountName + " was not found.")
			elif (response.status_code) == 429:
				print("The rate limit has been exceeded.  EXITING!")
				return;
			time.sleep(1.5)
	return;

def accountList():
	c = Counter(x['email'] for x in db)
	for k, v in c.items():
		print("{},  {}".format(k,v))

	return;

def accountExists(accountName):
	if db.search(Pwny.email == accountName):
		print("The account " + accountName + " exists in the database")
	else:
		print("The account " + accountName + " DOES NOT exist in the database")

def accountDetails(accountName):
	print("Details for " + accountName + "...")
	results = db.search(Pwny.email == accountName)
	for item in results:
		print(item['Name'])
		print(item['Description'])
		print()
	return;

def breachDetails(breachName):
	results = db.search(Pwny.Name == breachName)
	if len(results) > 0:
		print("Details for " + breachName + "...")
		breachResult = (results[0])
		print(breachResult['Description'])

	else:
		print("This breach was not found in the database.  Check the breach name.")
	return;

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-a", dest="addAccName", help="ADD account to database.  Support -v flag.")
	parser.add_argument("-b", dest="breachName", help="View details of particular BREACH.")
	parser.add_argument("-r", dest="remAccName", help="REMOVE account from database.")
	parser.add_argument("-c", help="COUNT accounts in database.", action="store_true")
	parser.add_argument("-s", help="Number of SITES in database.", action="store_true")
	parser.add_argument("-f", dest="filename", help="Bulk add accounts based on FILE.  One email address per line.")
	parser.add_argument("-l", help="List accounts in database", action="store_true")
	parser.add_argument("-e", dest="accExists", help="Determine if account is in database")
	parser.add_argument("-d", dest="accDet", help="Show details of specific account")
	parser.add_argument("-v", help="VERBOSE output. Display description of compromise", action="store_true")
	parser.add_argument("-g", help="GRAPH breaches to show greatest threat.", action="store_true")
	args = parser.parse_args()
	if (args.addAccName):
		addAccount(str(args.addAccName), args.v)
	if (args.breachName):
		breachDetails(str(args.breachName))
	if (args.remAccName):
		removeAccount(str(args.remAccName))
	if (args.c):
		totalAccounts()
	if (args.s):
		greatThreat()
	if (args.filename):
		bulkAccounts(str(args.filename))
	if (args.l):
		accountList()
	if (args.accExists):
		accountExists(str(args.accExists))
	if (args.accDet):
		accountDetails(str(args.accDet))
	if (args.g):
		graphThreat()

main()
