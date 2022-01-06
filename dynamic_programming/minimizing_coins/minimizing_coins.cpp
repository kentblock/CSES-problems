#include <iostream>
#include <algorithm>
#include <vector>

#define MAX 90000000000

using namespace std;

int minimizing_coins(int num_coins, vector<int> coins, int sum_size) {
    vector<long long> dp(sum_size + 1, MAX);
    dp[0] = 0;
    for (int i = 1; i < sum_size + 1; i++) {
        for (int j = 0; j < num_coins; j++) {
            int coin = coins[j];
            if (i - coin >= 0) {
                dp[i] =  min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[sum_size] == MAX ? -1 : dp[sum_size];
}

int main() {
    int sum, n;
    vector<int> coins(0);
    scanf("%d %d", &n, &sum);
    int i = 0;
    int coin;
    while (i < n) {
        scanf("%d", &coin);
        coins.push_back(coin);
        i++;
    }
    cout << minimizing_coins(n, coins, sum) << endl;
}