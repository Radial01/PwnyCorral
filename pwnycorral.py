from tinydb import TinyDB, Query, where
from termgraph.termgraph import chart
import json
import requests
from collections import Counter
import argparse
import time

User = Query()
db = TinyDB('db.json')
headers = {'User-Agent': 'PwnageDB'}

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
	db.remove(where('email') == accountName)
	print("Email address removed")
	return;

def totalAccounts():
	accTotal = 0
	c = Counter(x['email'] for x in db)
	print(len(set(c)))
	return;

def greatThreat():
	print("The site that poses the greatest threat is...")
	c = Counter(x['Name'] for x in db)
	print(type(c))
	for k, v in c.items():
		print("{} count:  {}".format(k,v))
	return;

def graphThreat():
	breachName_list = []
	breachCount_list = []

	c = Counter(x['Name'] for x in db)
	for k, v in c.items():
		breachName_list.append(k)
		breachCount_list.append([v])

	args = {'stacked': False, 'width': 50, 'no_labels': False, 'format': '{:<5.2f}', 'suffix': '', "vertical": False}
	chart(colors=[], data=breachCount_list, args=args, labels=breachName_list)

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
		print("{} count:  {}".format(k,v))

	return;

def accountExists(accountName):
	if db.search(User.email == accountName):
		print("The account " + accountName + " exists in the database")
	else:
		print("The account " + accountName + " DOES NOT exist in the database")

def accountDetails(accountName):
	print("Details for " + accountName + "...")
	results = db.search(User.email == accountName)
	for item in results:
		print(item['Name'])
		print(item['Description'])
		print()
	return;

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-a", dest="addAccName", help="ADD account to database.  Support -v flag.")
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
