# Pwny Corral

The intention of this script is to allow organizations
to determine which data breaches, after time, may be 
affecting their security posture.

## Getting Started



### Prerequisites

TinyDB
<<<<<<< HEAD
	pip install tinydb
Termgraph
	pip3 install termgraph
Requests
	pip install requests
=======
```
pip install tinydb
```
Termgraph
```
pip3 install termgraph
```
Requests
```
pip install requests
```
>>>>>>> b966058beb4c8a30e920254714a9566380e088cd

### Usage

Add account to database:
<<<<<<< HEAD
'''
Input:  python pwnycorral.py -a [email address]
'''

Remove account from database:

'''
Input:  python pwnycorral.py -r [email address]
'''

Display number of accounts in database:

'''
Input:  python pwnycorral.py -c
'''

Display number of pwned websites in database:

'''
Input:  python pwnycorral.py -s
'''
=======
```
Input:  python pwnycorral.py -a [email address]
```

Remove account from database:

```
Input:  python pwnycorral.py -r [email address]
```

Display number of accounts in database:

```
Input:  python pwnycorral.py -c
```

Display number of pwned websites in database:

```
Input:  python pwnycorral.py -s
```
>>>>>>> b966058beb4c8a30e920254714a9566380e088cd

Perform bulk load of email addresses into database.  The file should
contain one email address per line:

<<<<<<< HEAD
'''
Input:  python pwnycorral.py -f [FILENAME]
'''

List accounts in database:

'''
Input:  python pwnycorral.py -l
'''

Determine if account is in database:

'''
Input:  python pwnycorral.py -e [email address]
'''

Show details of specific account:

'''
Input:  python pwnycorral.py -d [email address]
'''

Display description of compromised site.  Can be used in conjuction with -a switch:

'''
Input:  python pwnycorral.py -v
'''

Create graph of breached sites and the number of compromised accounts that are part of each breach:

'''
Input:  python pwnycorral.py -g
'''
=======
```
Input:  python pwnycorral.py -f [FILENAME]
```

List accounts in database:

```
Input:  python pwnycorral.py -l
```

Determine if account is in database:

```
Input:  python pwnycorral.py -e [email address]
```

Show details of specific account:

```
Input:  python pwnycorral.py -d [email address]
```

Display description of compromised site.  Can be used in conjuction with -a switch:

```
Input:  python pwnycorral.py -v
```

Create graph of breached sites and the number of compromised accounts that are part of each breach:

```
Input:  python pwnycorral.py -g
```
>>>>>>> b966058beb4c8a30e920254714a9566380e088cd


## Authors

** Brad Dial **
