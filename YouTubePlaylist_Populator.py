#               Ram's YouTube Playlist Auto-Inserter
# __________________________________________________________________________________
#   The idea behind this is that I have a discord chat full of YouTube links
#     I wanted to get those links and auto populate them into a playlist.
#
# I used this program: https://github.com/Tyrrrz/DiscordChatExporter
#
# The program allows me to clone a chat into an HTML file
# then I rip as many links as possible, strip the Video ID and push them
# into Google's YouTube Data v3 API - namely the playlistItems().insert()
#
# Below is the documentation to get started with Google APIs
# https://developers.google.com/explorer-help/guides/code_samples#python
#
#
#
# Few things to note as you go through this:
# 1) using batches with Google's API doesn't work for ALL Google APIs, only
#       a select few - so of course the playlistItems got the boot
#
# 2) Regex output isn't perfect, so stripping and extracting are necessary for less bugs
#
# 3) File paths and IDs are hidden away in different folders, so that sketchy 
#    things don't happen when this code is ripped, but who is actually gonna 
#    go through all this and read it? :-)
#
#   For the "credentials" - if you're too lazy to edit the code in main they are
#       here as follows:
#       
#       Line 1) LocationPath - File path of your HTML file (AKA the discod chat)
#       Line 2) OutPutFile - Not necessary, but used for documentating all links found
#       Line 3) PlaylistID - You need this for the YouTube API
#

import re
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# This is something exclusively for the API
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def StrippingHTML(LocationPath, OutputFile):
    List_Links = [];
    x = open(LocationPath, 'rt', encoding="utf8")

    #quickly learned that all youtube vids have an 11 char ID
    reg = r'"https://www.youtube.com/watch\?v=.{11}?\"'

    for line in x:
        match = re.search(reg, line)
        if match: 
            List_Links.append(match.group(0))


    #removes repeats
    List_Links = list(set(List_Links))

    daf = open(OutputFile, "w")

    #cleaning before storing
    for writing in List_Links:
        writing = writing.strip('"')
        daf.write(writing)
        daf.write('\n')

    return List_Links


def Strip_Links_List(List_Links):
    VideoIDs = [];
    # 11:11 make a wish
    regg = r'/?v=.{11}?'

    for ID in List_Links:
        match = re.search(regg, ID)
        if match:
            # First we extract the VideoID
            temp = match.group(0)
            temp = temp[2:] 

            #Then we insert the VideoID into a list
            VideoIDs.append(temp)
    return VideoIDs




def InsertToPLaylist(VideoIDs, PlaylistID):
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json" # I swear I didn't name this

    daf = open("LogFile.txt", "w")

    # Get client secrets getting acquired
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Batch creation doesn't work entirely right with 
    # YouTube Data API v3 - doing manual executes for insert
    for VideoID in VideoIDs:
        request = youtube.playlistItems().insert(
                part="snippet,status",
                body={
                "snippet": {
                    "playlistId": PlaylistID,
                    "resourceId": {
                    "kind": "youtube#video",
                    "videoId": VideoID
                    }
                  }
                }
            ) 
        response = request.execute()
        print("Inserted Video ID: ", VideoID)
        daf.write(writing)
        daf.write('\n')

    # you know, cause testing...
    print("YouTube Playlist updated!")
        


def main():
    anon = input("Enter the file you wish to use: ")
    f = open(anon, "r")

    # Basically a credentials file 
    LocationPath = f.readline()
    OutputFile = f.readline()
    PlaylistID = f.readline()

    # readline() for whatever reason doesn't remove newlines...
    LocationPath = LocationPath.strip('\n')
    OutputFile = OutputFile.strip('\n')
    PlaylistID = PlaylistID.strip('\n')

    Links = StrippingHTML(LocationPath, OutputFile)
    
    VideoList = Strip_Links_List(Links)

    print("Finished list - going to insert function...")
    InsertToPLaylist(VideoList, PlaylistID)
    




main()
