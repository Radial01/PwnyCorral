# Pwny Corral
Pwny Corral is a Python script that queries the haveibeenpwned.com API in order to determine whether or not an account has been compromised.  Unlike many other scripts that perform this same function though, this script stores results.  The intention being to allow companies/organizations to identify trends in common sources of compromised accounts that may allow proactive measures to be taken before their security posture is greatly affected.

## Getting Started

Install TinyDB:  TinyDB is used to store the JSON returned from the haveibeenpwned response.  Before strorage of the JSON, Pwny Corral modifies each JSON response by adding the compromised email address to each response.
```
pip install tinydb
```
Install TermGraph:  Termgraph is used to graph the sites that have been breached along with the number of compromised accounts that exist in each.

```
pip3 install termgraph
```
Install Requests:  Requests allows the haveibeenpwned.com API request to take place.

```
pip install requests
```

## Using Pwny Corral

Add account to database:  This will query haveibeenpwned for a single email address.  If the email address is found to be compromised, the email address will be added to the JSON response and the response will be recorded to TinyDB.  
```
# python pwnycorral.py -a [email address]
```

Description of particular breach:  Command will query TinyDB for the description of a particular data breach.  Currently, the data breach name is case-sensitive.  For a listing of all current data breaches within TinyDB, try running Pwny Corral with the -s flag.
```

# python pwnycorral.py -b [name of breach site]
```

Remove account from database:  This command will remove an email address and it's associated data from TinyDB.
```

# python pwnycorral.py -r [email address]
```

Display number of accounts in database:  Display a count of accounts currently in your TinyDB.
```

# python pwnycorral.py -c
```

Display number of pwned websites in database:  Display a listing of breached websites that have been loaded into your TinyDB.  Useful if trying to find details of a particular breach using the -b flag.
```

# python pwnycorral.py -s
```

Bulk add email accounts:  Perform a bulk query against haveibeenpwned.  The supplied file should contain one email address per line.  The JSON response from haveibeenpwned will be updated to include the compromised email address and loaded into your TinyDB.
```

# python pwnycorral.py -f [FILENAME]
```
List accounts in database:  Displays a listing of all pwned accounts within your TinyDB.
```
# python pwnycorral.py -l
```

Determine if account is in database:  Command will check if email address currently exists within your TinyDB.  Currently, email address is case sensitive.
```

# python pwnycorral.py -e [email address]
```

Show details of specific account:  Command will query TinyDB and show all breaches this account has been a part of.
```

# python pwnycorral.py -d [email address]
```

Display description of compromised site:  Adding the -v flag to the "add account" command will display the compromised account details.
```

# python pwnycorral.py -a [email address] -v
```
Create graph:  Graph breached sites and the number of accounts that are a part of each breach.
```

# python pwnycorral.py -g
```
## Additional Information

For additional information, please see PwnyCorral-Instructions.pdf.

## Authors
Brad Dial
