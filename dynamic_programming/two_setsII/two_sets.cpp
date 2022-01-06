#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// knapsack problem 
// mod arithmetic rules to prevent overflow are a bit tricky

const int MOD = pow(10, 9) + 7;

int num_two_sets(int n) {
    int s = (n + 1) * n / 2;
    if (s & 1) {
        return 0;
    }
    int desired_sum = s / 2;
    vector<long long> dp(desired_sum + 1);
    dp[0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = desired_sum - i; j >= 0; j--) {
            dp[j + i] += dp[j];
            dp[j + i] %= 2 * MOD;
        }
    }
    return dp[desired_sum] / 2;
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
    cout << num_two_sets(read_num()) << endl;
}