from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

response = service.search().list(part = 'snippet', order = 'viewCount', q='lil uzi vert', type = 'video', maxResults = 10).execute()

searchItems = response['items']

request_body = {
    'snippet': {
        'title': 'Put Me On PlayList'
    }
}

newplaylist = service.playlists().insert(
                part='snippet',
                body = request_body
              ).execute()

newplaylistID = newplaylist['id']

for video in searchItems:
    request_body = {
        'snippet': {
            'playlistId': newplaylistID,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video['id']['videoId']
            }
        }
    }

    service.playlistItems().insert(
        part='snippet',
        body=request_body
    ).execute()