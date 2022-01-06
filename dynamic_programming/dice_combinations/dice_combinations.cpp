#include <iostream>
#include <cmath> 
#include <vector>
using namespace std;

int dice_combinations(int n) {
    int mod = pow(10, 9) + 7;
    vector<int> dp(n + 1);
    dp[0] = 1;
    for (int i = 0; i <= n; i++) {
        for (int j = 1; j <= 6; j++) {
            dp[i] += i - j >= 0 ? dp[i - j] : 0; 
            dp[i] %= mod;
        }
    }
    return dp[n];
}

int main() {
    int n;
    scanf("%d", &n);
    cout << dice_combinations(n) << endl;
}