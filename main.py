import csv
import numpy as np
import math
import random
from operator import itemgetter

print("Please wait while we initialize...")


def euclidean(a, b):
    l = len(a)

    val = 0

    for i in range(l):
        if (i-1) in range(5):
            continue
        val += (a[i]-b[0][i])**2

    val = math.sqrt(val)

    return val


def ifLike(reco):
    g = y[id[reco[2]], 0]

    gi = -1

    for i in range(len(genrelist)):
        if genrelist[i] == g:
            gi = i
    alpha = 0.08
    for j in range(30):
        myavg[gi][j] = alpha*(x[id[reco[2]]].tolist()[0][j]
                              ) + (1-alpha)*myavg[gi][j]


def ifDislike(reco, reason):

    if reason == "artist":
        dislikedArtist.append(y[id[reco[2]]].tolist()[0][2])
        return


def ifPlaylist(reco):
    g = y[id[reco[2]], 0]

    gi = -1

    for i in range(len(genrelist)):
        if genrelist[i] == g:
            gi = i

    alpha = 0.12

    for j in range(30):
        myavg[gi][j] = alpha*(x[id[reco[2]]].tolist()[0][j]
                              ) + (1-alpha)*myavg[gi][j]


def ifPlay(reco):
    g = y[id[reco[2]], 0]

    gi = -1

    for i in range(len(genrelist)):
        if genrelist[i] == g:
            gi = i

    alpha = 0.04

    for j in range(30):
        myavg[gi][j] = alpha*(x[id[reco[2]]].tolist()[0][j]
                              ) + (1-alpha)*myavg[gi][j]


r = csv.reader(open('tracks.csv', 'r', encoding='utf8'))
lst = list(r)
x = np.matrix(lst)
y = x[1:, 0:4]
x = x[1:, 4:].astype('double')

id = {}
dislikedArtist = []

for i in range(30):
    max = np.amax(x[:, i])
    min = np.amin(x[:, i])
    avg = sum(z.item(i) for z in x)
    diff = max-min
    x[:, i] = (x[:, i]-min)/diff

genrelist = []

for i in range(len(y)):
    id[y[i, 1]] = i
    if y[i, 0] not in genrelist:
        genrelist.append(y[i, 0])

timbre = [[0 for x in range(30)] for z in range(len(genrelist))]

cnt = [0 for z in range(len(genrelist))]

for j in range(len(genrelist)):
    for i in range(len(y)):
        if y[i, 0] == genrelist[j]:
            timbre[j] = [timbre[j][k]+x[i, k] for k in range(30)]
            cnt[j] = cnt[j]+1


timbre = [[timbre[i][j]/cnt[i] for j in range(30)]
          for i in range(len(genrelist))]


print('welcome to fitopsy')

like = []
dislike = []
playlist = []
ignore = []
visited = []
play = []

ignlen = 2
time = 0

print("genre list, choose give us the list of genres you like, comma sepearted")
print("1. rock\n2. punk\n3. folk\n4. pop\n5. dance and electronica\n6. metal\n7. jazz and blues\n8. classical\n9. hip-hop\n10. soul and reggae")
inp = input("Enter: ")
genres = inp.split(',')

genres = [int(genres[i]) for i in range(len(genres))]
myavg = [[0 for i in range(30)] for j in range(len(timbre))]
active = []
history = []

for i in range(len(genres)):
    myavg[genres[i]-1] = timbre[genres[i]-1]
    active.append(genres[i]-1)

lmt = 5
while len(history) < lmt:

    candidate = [[] for i in range(len(genres))]

    for i in range(len(active)):
        genre = genrelist[genres[i]-1]

        for j in range(len(x)):
            if y[j, 0] == genre:
                if y[j, 1] in visited:
                    continue
                dist = euclidean(myavg[active[i]], x[j, :].tolist())
                candidate[i].append((dist, j))

    candidate = [sorted(candidate[i], key=itemgetter(0))
                 for i in range(len(candidate))]

    recommend = []

    for i in range(len(genres)):
        for j in range(5):
            recommend.append(
                (y[candidate[i][j][1], 3], y[candidate[i][j][1], 2], y[candidate[i][j][1], 1], candidate[i][j][0]))

    recommend = sorted(recommend, key=itemgetter(3))
    print('here are your initial music recommendations based on your favorite genre')
    for i in range(len(recommend)):
        print(recommend[i][0], 'by', recommend[i][1])
        print("Enter your choice")
        print("1: Like")
        print("2: Dislike")
        print("3: Add to playlist")
        print("4: Ignore")
        print("5: Play")

        inp = int(input())

        if inp == 1:
            like.append((recommend[i], time))
            ifLike(recommend[i])
            visited.append(recommend[i][2])
            history.append((recommend[i][2], 2))
        elif inp == 2:
            print("Enter reason for disliking (artist/song):")
            ip = input()
            ifDislike(recommend[i], ip)
            dislike.append((recommend[i], time))
            visited.append(recommend[i][2])
        elif inp == 3:
            ifPlaylist(recommend[i])
            playlist.append((recommend[i], time))
            visited.append(recommend[i][2])
            history.append((recommend[i][2], 3))
        elif inp == 4:
            if len(ignore) < ignlen:
                ignore.append((recommend[i], time))
                visited.append(recommend[i][2])
            else:
                dslk = ignore.pop(0)
                visited.remove(dslk[0][2])
                ignore.append((recommend[i], time))
                visited.append(recommend[i][2])
        else:
            ifPlay(recommend[i])
            play.append((recommend[i], time))
            visited.append(recommend[i][2])
            history.append((recommend[i][2], 1))

while (True):

    recocnt = [0 for i in range(len(genrelist))]

    candidate = [[] for i in range(len(genrelist))]

    leng = len(candidate)

    for i in range(len(genrelist)):
        if i not in active:
            continue
        genre = genrelist[i]
        for j in range(len(x)):
            if y[j, 0] == genre:
                if (y[j, 1] in visited) or (y[j, 2] in dislikedArtist):
                    continue
                dist = euclidean(myavg[i], x[j, :].tolist())
                candidate[i].append((dist, j))

    if len(active) == len(genrelist):
        g1 = random.randint(0, len(genrelist)-1)

        g2 = random.randint(0, len(genrelist)-1)

        g1 = inactive[g1]
        g2 = inactive[g2]

        for j in range(len(x)):
            intgenre = -1
            for k in range(len(genrelist)):
                if genrelist[k] == y[j, 0]:
                    intgenre = k
            if intgenre == g1:
                if (y[j, 1] in visited) or (y[j, 2] in dislikedArtist):
                    continue
                dist = euclidean(myavg[g1], x[j, :].tolist())
                candidate[g1].append((dist, j))

        for j in range(len(x)):
            intgenre = -1
            for k in range(len(genrelist)):
                if genrelist[k] == y[j, 0]:
                    intgenre = k
            if intgenre == g2:
                if (y[j, 1] in visited) or (y[j, 2] in dislikedArtist):
                    continue
                dist = euclidean(myavg[g2], x[j, :].tolist())
                candidate[g2].append((dist, j))

        if g1 == g2:
            recocnt[g1] = 2
        else:
            recocnt[g1] = 1
            recocnt[g2] = 1

    else:
        inactive = []

        for i in range(len(genrelist)):
            if i not in active:
                inactive.append(i)

        g1 = random.randint(0, len(inactive)-1)
        g2 = random.randint(0, len(inactive)-1)

        g1 = inactive[g1]
        g2 = inactive[g2]

        for j in range(len(x)):
            intgenre = -1
            for k in range(len(genrelist)):
                if genrelist[k] == y[j, 0]:
                    intgenre = k
            if intgenre == g1:
                if (y[j, 1] in visited) or (y[j, 2] in dislikedArtist):
                    continue
                dist = euclidean(myavg[g1], x[j, :].tolist())
                candidate[g1].append((dist, j))

        for j in range(len(x)):
            intgenre = -1
            for k in range(len(genrelist)):
                if genrelist[k] == y[j, 0]:
                    intgenre = k
            if intgenre == g2:
                if (y[j, 1] in visited) or (y[j, 2] in dislikedArtist):
                    continue
                dist = euclidean(myavg[g2], x[j, :].tolist())
                candidate[g2].append((dist, j))

        if g1 == g2:
            recocnt[g1] = 2
        else:
            recocnt[g1] = 1
            recocnt[g2] = 1

    penalty = [[0 for i in range(len(candidate[j]))]
               for j in range(len(candidate))]

    for i in range(len(genrelist)):
        if i not in active:
            continue
        for j in range(len(candidate[i])):
            for k in range(len(dislike)):
                dslk = x[id[dislike[k][0][2]]]
                dist = euclidean(candidate[i][j], dslk.tolist())
                penalty[i][j] = penalty[i][j]+0.02/dist

    for i in range(len(candidate)):
        for j in range(len(candidate[i])):
            candidate[i][j] = list(candidate[i][j])
            candidate[i][j][0] = candidate[i][j][0] + penalty[i][j]
            candidate[i][j] = tuple(candidate[i][j])

    candidate = [sorted(candidate[i], key=itemgetter(0))
                 for i in range(len(candidate))]

    recommend = []

    l = int(len(history))

    score = [0 for i in range(len(genrelist))]
    totscore = 0

    for i in range(l-1, l-lmt-1, -1):
        g = y[id[history[i][0]]].tolist()[0][0]
        gi = -1
        for j in range(len(genrelist)):
            if genrelist[j] == g:
                gi = j

        score[gi] = score[gi]+history[i][1]

        totscore = totscore+history[i][1]

    mx = -1
    mxg = -1
    done = 0

    for i in range(len(genrelist)):
        if score[i] == 0:
            continue
        count = int(score[i]/totscore)*8

        if (count == 0):
            count = 1

        recocnt[i] = count

        done = done+count

        if mx < score[i]:
            mx = score[i]
            mxg = i

    recocnt[mxg] = recocnt[mxg]+8-done

    recommend = []

    for i in range(len(genrelist)):
        if recocnt[i] == 0:
            continue
        l = recocnt[i]
        if len(candidate[i]) < recocnt[i]:
            l = len(candidate[i])
        for j in range(l):
            recommend.append(
                (y[candidate[i][j][1], 3], y[candidate[i][j][1], 2], y[candidate[i][j][1], 1], candidate[i][j][0]))

    recommend = sorted(recommend, key=itemgetter(3))
    print('here are your 10 new music recommendations')
    for i in range(len(recommend)):
        print(recommend[i][0], 'by', recommend[i][1])
        print("Enter your choice")
        print("1: Like")
        print("2: Dislike")
        print("3: Add to playlist")
        print("4: Ignore")
        print("5: Play")

        inp = int(input())

        if inp == 1:
            like.append((recommend[i], time))
            ifLike(recommend[i])
            visited.append(recommend[i][2])
            history.append((recommend[i][2], 2))
        elif inp == 2:
            print("Enter reason for disliking (artist/song):")
            ip = input()
            ifDislike(recommend[i], ip)
            dislike.append((recommend[i], time))
            visited.append(recommend[i][2])
        elif inp == 3:
            ifPlaylist(recommend[i])
            playlist.append((recommend[i], time))
            visited.append(recommend[i][2])
            history.append((recommend[i][2], 3))
        elif inp == 4:
            if len(ignore) < ignlen:
                ignore.append((recommend[i], time))
                visited.append(recommend[i][2])
            else:
                dslk = ignore.pop(0)
                visited.remove(dslk[0][2])
                ignore.append((recommend[i], time))
                visited.append(recommend[i][2])
        else:
            ifPlay(recommend[i])
            play.append((recommend[i], time))
            visited.append(recommend[i][2])
            history.append((recommend[i][2], 1))
