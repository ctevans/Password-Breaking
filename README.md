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

####Cracked passwords:

#####Linux/Unix:

$LM$73cc52eafe696961:LATINI

$LM$fc738eb8b0e67616:TOOLBOX

$LM$1164ce4aaefc17ff:MICHELP

$LM$97a9eecee4b5f330:AKSS

$LM$f9c31a96c4c65b1e:X8SJKRO

Command Used: john --format=LM hashes_lanman.txt

F9C31A96C4C65B1E97A9EECEE4B5F330:X8SJKROAKSS

FC738EB8B0E67616AAD3B435B51404EE:TOOLBOX

1164CE4AAEFC17FF73CC52EAFE696961:MICHELPLATINI

Note that AAD3B435B51404EE is the hash of an all null 7 character half.

#####Windows/LANMAN:

$NT$f3f69a51fc702f24ee994a3a98fca9b0:toolbox

$NT$4b5628becfd9ad0bc1a5e797ff3ca686:x8SJkrOAksS

$NT$d94631ab52f49e06830bd207da175d32:MichelPlatini




For further information please look at the report document in the repo.
