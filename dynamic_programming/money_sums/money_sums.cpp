#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

// Classic knapsack problem

void money_sums(vector<int> coins) {

    int max_sum = accumulate(coins.begin(), coins.end(), 0);
    vector<bool> dp(max_sum + 1);
    dp[0] = true;
    for (int i = 0; i < coins.size(); i++) {
        int coin = coins[i];
        for (int j = max_sum - coin; j >= 0; j--) {
            dp[j + coin] = dp[j] | dp[j + coin];
        }
    }

    cout << count(dp.begin(), dp.end(), true) - 1 << endl;

    for (int i = 1; i < max_sum + 1; i++) {
        if (dp[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
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

    vector<int> coins = read_nums(read_num());
    money_sums(coins);
}