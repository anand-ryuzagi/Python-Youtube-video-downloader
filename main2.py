#pafy module
import pafy

#downloading best resolution video

url = input("copy and paste the youtube video link : ").strip()
video = pafy.new(url) 

streams = video.streams 
for i in streams: 
	print(i) 
	
# get best resolution regardless of format 
best = video.getbest() 

print(best.resolution, best.extension) 

# Download the video 
best.download() 
