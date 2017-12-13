import os
import re
from threading import Thread

##############
# Outputs stats for each user_id : number of media / comments
##############

# Files for each type of data
media_files = []
comments_files = []
dataset_dir = './dataset_sample'
for root, dirs, files in os.walk(dataset_dir):
    for filename in files:
        if re.match('media_\d', filename) != None:
            media_files.append(dataset_dir + "/" + filename)
            continue
        if re.match('media_comments_\d', filename) != None:
            comments_files.append(dataset_dir + "/" + filename)
            continue


class Reader(Thread):

    def __init__(self, files, field, table):
        Thread.__init__(self)
        self.files = files
        self.field = field
        self.table = table
    
    def run(self):
        for filename in self.files:
            print "Processing file: " + filename
            with open(filename) as f:
                for l in f.readlines():
                    a = l.split('|')
                    uid = a[self.field]
                    if uid not in self.table.keys():
                        self.table[uid] = 1
                    else:
                        self.table[uid] += 1

# Tables for collecting results
user_nbposts = {}
user_nbcomments = {}

thread1 = Reader(media_files, 0, user_nbposts)
thread2 = Reader(comments_files, 3, user_nbcomments)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


# Gen stats
nb_0post = 0
nb_25post = 0
nb_50post = 0
nb_75post = 0
nb_100post = 0
nb_postonly = 0

uids = set(user_nbposts.keys()) | set(user_nbcomments.keys())
for uid in uids:
    if (uid in user_nbposts.keys()) & (uid not in user_nbcomments.keys()):
        nb_postonly += 1
        continue
    if (uid not in user_nbposts.keys()) & (uid in user_nbcomments.keys()):
        nb_0post += 1
        continue
    nb_post = user_nbposts[uid]
    nb_comments = user_nbcomments[uid]
    nb_req = nb_post + nb_comments
    pc_post = float(nb_post/nb_req) * 100
    if pc_post <= 25:
        nb_25post += 1
        continue
    if pc_post <= 50:
        nb_50post += 1
        continue
    if pc_post <= 75:
        nb_75post += 1
        continue
    else:
        nb_100post += 1

print "Number of user with 0 post: " + str(nb_0post)
print "Number of user  <25\% post: " + str(nb_25post)
print "Number of user 25\%-50% post: " + str(nb_50post)
print "Number of user 50\%-75% post: " + str(nb_75post)
print "Number of user 75\%-100% post: " + str(nb_100post)
print "Number of user post-only: " + str(nb_postonly)
