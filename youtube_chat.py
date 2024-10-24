import os
import json
import time
import random
from googleapiclient.discovery import build
from scripts.youtube_auth import Authorize

authResponse = Authorize(os.path.dirname(os.path.realpath(__file__)) + '/scripts/client_secret.json')
credentials = authResponse.credentials

# Building the youtube object:
youtube = build('youtube', 'v3', credentials=credentials)

# Settings
_delay = 20
youtube_log_filepath = 'youtube_chat_log.txt'


def getLiveChatId(LIVE_STREAM_ID):
    """
    It takes a live stream ID as input, and returns the live chat ID associated with that live stream

    LIVE_STREAM_ID: The ID of the live stream
    return: The live chat ID of the live stream.
    """

    stream = youtube.videos().list(
        part="liveStreamingDetails",
        id=LIVE_STREAM_ID,  # Live stream ID
    )
    response = stream.execute()
    # print("\nLive Stream Details:  ", json.dumps(response, indent=2))

    liveChatId = response['items'][0]['liveStreamingDetails']['activeLiveChatId']
    print("\nLive Chat ID: ", liveChatId)
    return liveChatId


# Access user's channel Name:
def getUserName(userId):
    """
    It takes a userId and returns the userName.

    userId: The user's YouTube channel ID
    return: User's Channel Name
    """
    channelDetails = youtube.channels().list(
        part="snippet",
        id=userId,
    )
    response = channelDetails.execute()
    # print(json.dumps(response, indent=2))
    userName = response['items'][0]['snippet']['title']
    return userName
# print(getUserName("UC0YXSy_J8uTDEr7YX_-d-sg"))


def start_youtube_bot():
    LIVE_STREAM_ID = input("Enter the live stream ID: ")
    # LIVE_STREAM_ID = "zxJ01IK_9z0"
    liveChatId = getLiveChatId(LIVE_STREAM_ID)
    messagesList = []  # List of messages

    while True:
        # bot replies to every message within past 1 second (can be changed to add delay):
        time.sleep(_delay)

        notReadMessages = []  # List of messages not yet read by bot

        # Fetching the messages from the live chat:
        liveChat = youtube.liveChatMessages().list(
            liveChatId=liveChatId,
            part="snippet"
        )
        response = liveChat.execute()
        # print("\nMessages Fetched:  ", json.dumps(response, indent=2))
        allMessages = response['items']


        
        # Check if there are any new messages and add them messagesList/notReadMessages list:
        # if len(messagesList) >= 0:
        #     for messages in allMessages:
        #         userId = messages['snippet']['authorChannelId']
        #         message = messages['snippet']['textMessageDetails']['messageText']
        #         messagesList.append((userId, message))
        # else:
        for messages in allMessages:
            userId = messages['snippet']['authorChannelId']
            message = messages['snippet']['textMessageDetails']['messageText']
            if (userId, message) not in messagesList:
                messagesList.append((userId, message))
                notReadMessages.append((userId, message))

        for message in notReadMessages:
            userId = message[0]
            message = message[1]
            userName = getUserName(userId)
            with open(youtube_log_filepath,'a') as f:
                f.write(message + '\n')

if __name__ == "__main__":
    start_youtube_bot()
