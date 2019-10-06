import instaloader
L = instaloader.Instaloader()

username = 'ustadzkuh' 
password = 'bekasi123' 
L.login(username, password)


instagram_target = 'ahmad.badruzaman' 
profile = instaloader.Profile.from_username(L.context, instagram_target)

follow_list = []
likes_list = []
comments_list = []
count = 1
file = open("instagram_followers.txt","w")
for followee in profile.get_followers():
    username = followee.username
    like = get_likes.like
    comment = get_comments.comment
    file.write(str(count) + ". " + username + likes + comment + "\n")
    print(str(count) + ". " + username + like + comment )
    count = count + 1


print("selesai")
file.close()
