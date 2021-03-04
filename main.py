# importing module 
import youtube_dl 

ydl_opts = {} 

def download_video(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
		ydl.download([link]) 

channel = 1
while (channel == int(1)): 
	link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ") 
	link = link_of_the_video.strip() 

	download_video() 
	channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done ")) 
