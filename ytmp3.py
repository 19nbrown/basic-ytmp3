import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',   # get the best audio stream
        'outtmpl': '%(title)s.%(ext)s',  # save as video title
        'postprocessors': [{  # convert to mp3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    link = input("Enter YouTube link: ")
    download_audio(link)
