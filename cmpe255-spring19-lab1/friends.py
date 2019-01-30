users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    name = list(filter(lambda person: person['id'] == user, users))[0].get('name')
    count=0
    for item in friendship:
        count += item.count(user)
    print(name + ' has ' + str(count) + ' friends')

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    friend_list = []
    for user in users:
        user_id = user.get('id')
        count=0
        for item in friendship:
            count += item.count(user_id)
        friend_list.insert(user_id,(list(filter(lambda person: person['id'] == user_id, users))[0].get('name'),count))
    friend_list.sort(key=lambda x: x[1],reverse = True)
    for f in friend_list:
        print(f[0] + ' has ' + str(f[1]) + ' friends')

if __name__ == "__main__":
    user_input = input('Please enter the user id: ')
    num_friends(int(user_input))
    print('\nSorting by number of friends...')
    sort_by_num_friends()
