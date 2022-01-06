#include <iostream>
#include <vector>
using namespace std;
#define MAX_CUTS 10000001

long long rectangle_cutting(int width, int height) {
    vector<vector<long long> > dp(width + 1, vector<long long>(height + 1, MAX_CUTS));
    for (int k = 0; k < min(width, height) + 1; k++) {
        dp[k][k] = 0;
    }
    for (int i = 1; i < dp.size(); i++) {
        for (int j = 1; j < dp[0].size(); j++) {
            for (int k = 1; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k] + 1);
            }
            for (int k = 1; k < i; k++) {
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1);
            }
        }
    }
    return dp[width][height];
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
    cout << rectangle_cutting(read_num(), read_num()) << endl;
}