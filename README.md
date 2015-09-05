# spencer1M
a python script which sends an email when a specific youtuber reaches a number of subscribers 

In this case, when the youtuber SpencerFC (username = officialfifaplaya) reaches 1 million subscribers, an email is sent to 2 recipients

This code needs to constantly be running so I configured an smtp server on my raspberry pi and kept it running. Ran using 'nohup python run.py &' since this keeps the script running even when I log out of SSH. 
