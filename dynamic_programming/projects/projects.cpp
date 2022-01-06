#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

// TODO get this working

/*

int comp_projects(tuple<int, int, int> p1, tuple<int, int, int> p2) {
    return get<1>(p1) < get<2>(p2);
}

int find_index(vector<tuple<int, int, int> > projects, int start_time, int e) {
    int s = 0;
    while (s < e) {
        int mid = (s + e) / 2 + ((s + e) % 2 != 0);
        if (get<1>(projects[mid]) >= start_time) {
            e = mid - 1; 
        } else {
            s = mid;
        }
    }
    return get<1>(projects[s]) < start_time ? s : -1; 
}


long long max_projects(vector<tuple<int, int, int> > projects) {
    vector<long long> dp(projects.size());
    sort(projects.begin(), projects.end(), comp_projects);
    for (int i = 1; i < projects.size(); i++) {
        int start, end, money;
        tie(start, end, money) = projects[i];
        int last_project_index = find_index(projects, start, i - 1);
        dp[i] = max(dp[i - 1], last_project_index == -1 ? money : money + dp[last_project_index]);
    }
    return dp[dp.size() - 1];
}

int read_num() {
    int num;
    scanf("%d", &num);
    return num;
}

int main() {
    int n = read_num();
    vector<tuple<int, int, int> > projects;
    while (n--) {
        projects.push_back(make_tuple(read_num(), read_num(), read_num()));
    }
    cout << max_projects(projects) << endl;
}

*/