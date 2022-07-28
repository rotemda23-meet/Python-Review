title = input("what is the title of your video sweetheart?")
description = input("sorry but only one more question, i need you to right a dscription of your video..")
def create_youtube_video(title,description):
	video = {"title" : title , "description" : description , "likes" : 0 , "dislikes" : 0 , "comments" : {} }
	return video

def like(dict):
    if "likes" in dict:
    	dict["likes"] = dict["likes"] + 1
    return dict

def disLike(dict):
    if "dislikes" in dict:
    	dict["dislikes"] = dict["dislikes"] + 1
    return dict

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

new_video = create_youtube_video("song", "amazing song")
for i in range(495):
	new_video = like(new_video)
new_video = disLike(new_video)
new_video = add_comment(new_video, "rotem", "wow")
new_video = add_comment(new_video, "shai", "omg")
print(new_video)
