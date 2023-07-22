from pytube import Playlist

# Ask the user for the playlist URL
url = input("Enter the YouTube playlist URL: ")

# Create a Playlist object and extract the videos
pl = Playlist(url)
videos = pl.video_urls

# Download each video
for i, video in enumerate(videos):
    print(f"Downloading video {i+1} of {len(videos)}...")
    yt = YouTube(video)
    stream = yt.streams.get_highest_resolution()
    stream.download()
print("Download complete!")
