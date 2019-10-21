import instaloader
import csv
L = instaloader.Instaloader()

username = "mhmd_ridwan"
password = "ridwantuper123"
L.login(username, password)

target = 'arzi_mu'
profile = instaloader.Profile.from_username(L.context, target)

file = open("data instagram" + ".csv","w+")
kolom = ['account', 'post', 'tag', 'likes', 'comments']
writer = csv.DictWriter(file, fieldnames=kolom)
writer.writeheader()
follow_list = []

for followee in profile.get_followers():
    print ('------------------------------')
    username = followee.username
    profile = instaloader.Profile.from_username(L.context, username)
    print(profile)
    count = 1
    print("post, hashtag and comments")
    for post in profile.get_posts():
        print(username, str(count), 'dari', str(profile.mediacount))
        if post.caption is not None:
            count += 1
            captions = post.caption.encode('ascii', 'ignore').decode('ascii')
            hashtag = post.caption_hashtags
            like = post.likes #int
            comment = post.get_comments()
            daftar_comments = []
            for ig_comment in comment:
                komentar = ig_comment.text.encode('ascii', 'ignore').decode('ascii')
                daftar_comments.append(komentar)
            data = {"account": username, "post":captions, "tag":hashtag, "likes":str(like), "comments":daftar_comments}
            follow_list.append(data)
            writer.writerow(data)


file.close()
