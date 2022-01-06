from sys import stdin

# Works but just barely TLE on CSES, use C++

def max_projects(projects):
    projects.sort(key=lambda x: x[1])
    dp = [0 for _ in range(len(projects))]
    for i in range(len(dp)):
        start, _, money = projects[i]
        index = find_latest(projects, start, i - 1) if i else -1
        dp[i] = max(dp[i - 1], money if index == -1 else money + dp[index])
    return dp[-1]

def find_latest(projects, start_time, e):
    s = 0
    while s < e:
        mid = -(-(s + e) // 2)
        if projects[mid][1] >= start_time:
            e = mid - 1
        else:
            s = mid
    return s if projects[s][1] < start_time else -1        

def read_num():
    return int(stdin.readline())


if __name__ == '__main__':
    _ = read_num()
    projects = []
    for line in stdin.readlines():
        projects.append(tuple([int(num) for num in line.split()]))
    print(max_projects(projects))