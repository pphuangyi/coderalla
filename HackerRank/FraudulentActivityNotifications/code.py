def get_median(memo, d):
    count = 0
    if d % 2 == 1:
        for key, val in memo.items():
            count += val
            if count > d // 2:
                return key
    else:
        left = None
        for key, val in memo.items():
            count += val
            if count >= d // 2 + 1:
                if left is None:        
                    return key
                else:
                    return (left + key) / 2
            elif count == d // 2:
                left = key


def activityNotifications(expenditure, d):
 
    memo = {e: 0 for e in range(201)}   
    for e in expenditure[:d]:
        memo[e] += 1
    
    num_notifications = 0
    for day in range(d, len(expenditure)):
        median = get_median(memo, d)
        print(memo)
        print(median)
        if expenditure[day] >= 2 * median:
            num_notifications += 1
        memo[expenditure[day - d]] -= 1
        memo[expenditure[day]] += 1
    
    return num_notifications
        

if __name__ == '__main__':
    with open('data/input01.txt', 'r') as handle:
        n, d = list(map(int, handle.readline().strip().split()))
        expenditure = list(map(int, handle.readline().strip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
