#!/usr/bin/python
# coding: utf-8

from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


# 欧几里得距离
def sim_distance(prefs, person1, person2):
    common_data = filter(lambda x: x in prefs[person2], prefs[person1].keys())
    if len(common_data) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in common_data])
    return 1 / (1 + sqrt(sum_of_squares))


# 皮尔逊相关度
def sim_pearson(prefs, person1, person2):
    common_data = filter(lambda x: x in prefs[person2], prefs[person1].keys())

    n = len(common_data)
    if n == 0:
        return 0

    # sum all
    sum1 = sum([prefs[person1][item] for item in common_data])
    sum2 = sum([prefs[person2][item] for item in common_data])

    # sum all square
    sum1Sq = sum([pow(prefs[person1][item], 2) for item in common_data])
    sum2Sq = sum([pow(prefs[person2][item], 2) for item in common_data])

    # sum product
    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in common_data])

    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    return num / den


if __name__ == "__main__":
    print sim_distance(critics, "Lisa Rose", "Gene Seymour")
    print sim_pearson(critics, "Lisa Rose", "Gene Seymour")
