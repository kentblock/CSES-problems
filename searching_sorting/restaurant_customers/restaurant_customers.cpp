#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

int max_customers(vector<pair <int, char> > times) {
    sort(times.begin(), times.end());
    int max_customers = 0;
    int cur_max = 0;
    for (int i = 0; i < times.size(); i++) {
        cur_max += times[i].second == 'A' ? 1 : -1;
        max_customers = max(cur_max, max_customers);
    }
    return max_customers;
}

int main() {
    int n;
    scanf("%d", &n);
    int a_time, d_time;
    vector <pair <int, char> > times;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a_time, &d_time);
        times.push_back(make_pair(a_time, 'A'));
        times.push_back(make_pair(d_time, 'D'));
    }
    cout << max_customers(times) << endl;
}

