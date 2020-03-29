# Corona-BOT
I created a corona virus notifier bot. which notifies about the current statistics by posting them on a slack notifications,

This notifies about the cases of coronovirus by scrapping the data from https://www.mohfw.gov.in (official)

The main file is corona_bot.py

When it is run,

1The data is scrapped from this website,

2)Data is Tabulated with tabulate library

3)That data is stored in a json file,

3)Slacker fetches the data from json and posts it to slack.


you can get notified by the slack channel from here - https://join.slack.com/t/techgag/shared_invite/zt-czm5dmtu-OemmhblGNpih9AEPC~4vjg
