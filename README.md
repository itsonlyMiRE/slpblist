# slpblist
ever have such an unpleasant experience versus someone on slippi unranked that you want to make sure you never have to play them again? blacklist slippi codes! block toxicity! a simple script that plays an alert sound when you're matched against a person on your blacklist.

# info
this python script is designed to run in the background while you queue unranked. after downloading the repo, open `slpblist.txt` and replace the first line with the path to your .slp file folder, and place one connect code on each new line after that - should look like:
```
E:\slp-files\
mire#409
mire#409
mire#409
```

then run the script with `python3 ./slpblist.py`

the script is regularly checking your .slp folder for new files (created when a new match starts). once a new file is found it is parsed for connect codes; an alert sound is played if their code is found in your blacklist.

currently only works on windows