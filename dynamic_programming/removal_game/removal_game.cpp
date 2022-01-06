#include <iostream>
#include <vector>

using namespace std;

long long removal_game(vector<int> nums) {
    bool turn = nums.size() & 1;
    vector<vector<long long> > dp(nums.size(), vector<long long>(nums.size()));
    for (int k = 0; k < nums.size(); k++) {
        dp[k][k] = turn ? nums[k] : 0;
    }

    for (int i = nums.size() - 1; i >= 0; i--) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (turn == ((i - j + 1) & 1)) {
                dp[i][j] = max(
                    dp[i + 1][j] + nums[i],
                    dp[i][j - 1] + nums[j]
                );
            } else {
                dp[i][j] = min(
                    dp[i + 1][j],
                    dp[i][j - 1]
                );
            }
        }
    }
    return dp[0][nums.size() - 1];
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
    cout << removal_game(read_nums(read_num())) << endl;
}