import instaloader
import csv

loginData = open('login', 'r').readlines()
EMAIL = loginData[0][:-1]
PASSWORD = loginData[1]

L = instaloader.Instaloader()

L.login(EMAIL, PASSWORD)
print('Logged in succesfully')


SHORTCODES = ['CRoOlIMhoE8', 'CRyBLj7hXHa', 'CR6d-IxBrOS', 'CR_U5NzMQPr', 'CSHrV6LLWK0', 'CR6pGbvghAN', 'CR1ZNdLjfm9', 'CRoQ3inDUil'] #Can later be extracted from links from external file

for shortcode in SHORTCODES:
    likes_file = f'insta_likes_{shortcode}.csv'
    comments_file = f'insta_comments_{shortcode}.csv'

    post = instaloader.Post.from_shortcode(L.context, shortcode)
    post_likes = post.get_likes()
    post_comments = post.get_comments()

    #Importing likes to csv
    likesFile = open(likes_file, 'w')
    writer = csv.writer(likesFile)
    writer.writerow(['post-shortcode', 'username'])
    for like in post_likes:
        writer.writerow([shortcode, like.username])
    likesFile.close()

    #Importing comments to csv
    commentFile = open(comments_file, 'w')
    writer = csv.writer(commentFile)
    writer.writerow(['post-shortcode', 'comment'])
    for comment in post_comments:
        writer.writerow([shortcode, comment.owner.username])
    commentFile.close() #todo: 1 loop for likes and comments

#Importing usernames of followers to csv
PROFILE_NAMES = ['https://www.instagram.com/vetti.art', 'vetti.art', 'nounsinse', 'drawing_dalia', 'pandore.necrotic']

for name in PROFILE_NAMES:
    followers_file = f'insta_followers_{name}.csv'
    profile = instaloader.Profile.from_username(L.context, name)
    followerNames = profile.get_followers()

    followerFile = open(followers_file, 'w')
    writer = csv.writer(followerFile)
    writer = writerow(['account name', 'follower name'])
    for follower in followerNames:
        writer.writerow([name, follower])
    followerFile.close()