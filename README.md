# Pwny Corral

This script queries the HaveIBeenPwned.com API to determine if an account has been breached.  
The intention of this script is to allow organizations to determine which data breaches, after time, may be 
affecting their security posture.

### Prerequisites

TinyDB
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

### Usage

Add account to database:
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

Perform bulk load of email addresses into database.  The file should
contain one email address per line:
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

## Authors

** Brad Dial **
