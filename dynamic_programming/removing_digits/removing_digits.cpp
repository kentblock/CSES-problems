#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int removing_digits_memo(int num, vector<int> dp) {
    if (num < 0) {
        return INT32_MAX;
    }
    if (dp[num] != -1) {
        return dp[num];
    }
    int result = INT32_MAX;
    int digits = num;
    while (digits) {
        int digit = (digits % 10);
        if (digit) {
            result = min(result, removing_digits_memo(num - digit, dp) + 1);
        }
        digits /= 10;
    }
    dp[num] = result;
    return result;
}

int read_num() {
    int num;
    scanf("%d", &num);
    return num;
}

int main() {
    int n = read_num();
    vector<int> dp(n + 1, -1);
    dp[0] = 0;
    cout << removing_digits_memo(n, dp) << endl;
}