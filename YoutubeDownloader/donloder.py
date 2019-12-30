from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# data donlot + config ?

download_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

# lokasi donlot

if not os.path.exists('Songs'):
	os.mkdir('Songs')
else:
	os.chdir('Songs')

# Download Songs

with youtube_dl.YoutubeDL(download_options) as dl:
	with open('../' + argv[1], 'r') as f:
		for song_url in f:
			dl.download([song_url])