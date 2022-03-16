"""Restaurant rating lister."""


# put your code here
def getRatings():
    ratings = {}
    with open('core-python\scores.txt') as ratingsData:
        for line in ratingsData:
            shop, rating = line.partition(':')[::2]
            ratings[shop.strip()] = int(rating)
    # print(ratings)
    sortednames=sorted(ratings.keys(), key=lambda x:x.lower())
    for i in sortednames:
        values=ratings[i]
        # print('Shop Name = ' + i)
        # print('Rating Value = ' + str(values))
        print(i + ' is rated at ' + str(values))
    ratingsData.close()

newShop= input("What shop would you like to add?\n")
newRating = input("What would you rate that shop?\n")
txt=open('core-python\scores.txt', 'a')
txt.write('\n' + newShop + ': ' + newRating)
txt.close()
getRatings()