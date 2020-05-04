# Corona-BOT
I created a corona virus notifier bot, which notifies about the current statistics by posting them as slack notifications.

It notifies about the cases of coronovirus by scrapping the data from https://www.mohfw.gov.in
and then the scrapped data is displayed as a Tabular Slack Notification.

## The main file is corona_bot.py

When it is run,

- The data is scrapped from this website,

 - Data is Tabulated with tabulate library

- That data is stored in a json file,

- Slacker fetches the data from json and posts it to slack.


you can get notified by the slack channel from [here](https://join.slack.com/t/techgag/shared_invite/zt-czm5dmtu-OemmhblGNpih9AEPC~4vjg)
