#include <array>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define MAX_LEN 5001

array<array<int, MAX_LEN>, MAX_LEN> dp = { };

int min_edit_distance(string s1, string s2) {
    for (int i = 0; i < s1.length() + 1; i++) {
        for (int j = 0; j < s2.length() + 1; j++) {
            if (!i) {
                dp[i][j] = j;
            } else if (!j) {
                dp[i][j] = i;
            } else if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
            }
        }
    }
    return dp[s1.length()][s2.length()];
}

int main() {
    char s1[MAX_LEN], s2[MAX_LEN];
    scanf("%s", &s1);
    scanf("%s", &s2);
    cout << min_edit_distance(string(s1), string(s2)) << endl;
}