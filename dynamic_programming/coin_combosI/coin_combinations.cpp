#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int MOD = pow(10, 9) + 7;
const int MAX_COINS = 100;

long long coin_combinations(int num_coins, int coins[], int sum_size) {
    long long dp[sum_size + 1];
    dp[0] = 1;
    for (int i = 1; i < sum_size + 1; i++) {
        dp[i] = 0;
        for (int j = 0; j < num_coins; j++) {
            int coin = coins[j];
            if (i - coin >= 0) {
                dp[i] += dp[i - coin];
                dp[i] %= MOD;
            }
        }
    }
    return dp[sum_size];
}

int main() {
    int n, sum_size;
    int coins[MAX_COINS];
    scanf("%d %d", &n, &sum_size);
    for (int i = 0; i < n; i++) {
        scanf("%d", &coins[i]);
    }
    cout << coin_combinations(n, coins, sum_size) << endl;
}