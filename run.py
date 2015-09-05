from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyA0kLPG3WHvA1tCdLsH5TuWiNMnR7SUxVI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

subscription_feed = yt_service.GetYouTubeSubscriptionFeed(username='spencerFC')

if isinstance(subscription_feed, gdata.youtube.YouTubeSubscriptionFeed)):
  # given a YouTubeSubscriptionEntry we can determine it's type (channel, favorite, or query)
	for entry in subscription_feed.entry:
		print entry.GetSubscriptionType()
