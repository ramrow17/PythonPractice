# Ram's YouTube Playlist Auto-Inserter
# Below is the documentation to get started with Google APIs
# https://developers.google.com/explorer-help/guides/code_samples#python






import os
import sys

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

VideoIDs = ['Lb2EmdLOZ10', '_KO50UmcZl8', '47Plg93oJ1M']
PlaylistID = "PL7qhHmCShbjwQY7ncowP_i8mG5zS_8Crb"

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = ClientSecret

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    sys.exit("Testing done!")

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

    print(response)

if __name__ == "__main__":
    main()