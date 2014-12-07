'''
Created on 2013-9-28

@author: Administrator
'''

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, 
                      "Norah Jones": 4.5, "Phoenix": 5.0,"Slightly Stoopid": 1.5,
                      "The Strokes": 2.5, "Vampire Weekend": 2.0
                    },
"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
"Deadmau5": 4.0, "Phoenix": 2.0,
"Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
"Deadmau5": 1.0, "Norah Jones": 3.0,
"Phoenix": 5, "Slightly Stoopid": 1.0},
"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
"Deadmau5": 4.5, "Phoenix": 3.0,
"Slightly Stoopid": 4.5, "The Strokes": 4.0,
"Vampire Weekend": 2.0},
"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
"Norah Jones": 4.0, "The Strokes": 4.0,
"Vampire Weekend": 1.0},
"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
"Phoenix": 5.0, "Slightly Stoopid": 4.5,
"The Strokes": 4.0, "Vampire Weekend": 4.0},
"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
"Norah Jones": 3.0, "Phoenix": 5.0,
"Slightly Stoopid": 4.0, "The Strokes": 5.0},
"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
"Phoenix": 4.0, "Slightly Stoopid": 2.5,
"The Strokes": 3.0}}

print users['Veronica']


def manhattan(rating1, rating2):
#    print rating1,rating2
    
    distance = 0
    for key in rating1:
        if key in rating2:
#            print key
            distance += abs(rating1[key] - rating2[key])
            
    return distance


def nearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
            
    distances.sort()
    return distances;
    

def recommend(username, users):
    
    nearest = nearestNeighbor(username, users)[0][1]
    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
     
    return sorted(recommendations,key= lambda tup: tup[1], reverse = True)
            
print recommend('Hailey', users)           
    
    
