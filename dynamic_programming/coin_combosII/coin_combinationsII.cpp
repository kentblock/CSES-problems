#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
const int MOD = pow(10, 9) + 7;

int ordered_coin_combinations(vector<int> coins, int desired_sum) {
    sort(coins.begin(), coins.end());
    vector<long long> dp(desired_sum + 1);
    dp[0] = 1;
    for (int i = 0; i < coins.size(); i++) {
        int coin = coins[i];
        for (int j = 0; j + coin <= desired_sum; j++) {
            dp[j + coin] += dp[j];
            dp[j + coin] %= MOD;
        }
    }
    return dp[desired_sum];
}

vector<int> read_nums(int size) {
    vector<int> nums(size);
    for (int i = 0; i < size; i++) {
        int num;
        scanf("%d", &num);
        nums[i] = num;
    }
    return nums;
}

int read_num() {
    int num;
    scanf("%d", &num);
    return num;
}

int main() {
    int size = read_num();
    int desired_sum = read_num();
    vector<int> coins = read_nums(size);
    cout << ordered_coin_combinations(coins, desired_sum) << endl;
}