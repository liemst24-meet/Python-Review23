def create_youtube_video(title, description):
	youtube_video = {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text 
	return youtubevideo

my_video = create_youtube_video("I bought the queen ov englang", "she is alive")
for i in range(495):
	my_video = like(my_video)

my_video = dislike(my_video)

print(my_video)