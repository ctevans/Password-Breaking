# Password-Breaking

Language: Python 3
Tools: John the Ripper http://www.openwall.com/john/

##Overview:
Given Unix/Linux and Windows/LANMAN password hashes, the goal is to crack the original passwords used!
(Note: With heavy computational power restrictions, we couldn't use something like a server to do this!)


####Ideas:
Spread out across multiple python files, we will be taking a massive dictionary of words and we will be churning through the entire thing and for each possible word we will be making numerous modifications to the word and attempt to find a match to the hash we were given.

Why would we do such a thing? An ideal hash will be collision resistant (ontop of many other ideal security properties I shouldn't go into here!).

####Configure John The Ripper.
Because a tool is nice, but a tool is only as effective as how you use it!
So we obtained a novel configuration file: john.conf.txt

####Have a Python program (We have 3) deal with filtering through the dictionary and breaking the passwords.

cities.py:

cased10.py:

leeter.py:


For further information please look at the report document in the repo.
