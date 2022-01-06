#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

long long MOD = pow(10, 9) + 7;

// Intuition: 6 cases for what the top row of the tower looks like 
// Case: 0) '  ', 1) ' | ', 2) '-| ', 3) '--', 4) ' |-', 5) '-|-'
// Top of tower must be case 3 or 5
void count_towers(int largest_height, vector<vector<long long> > &towers) {
    towers[0][3] = 1;
    for (int i = 1; i < largest_height + 1; i++) {
        for (int j = 0; j < 6; j++) {
            if (j == 0 || j == 3) {
                towers[i][j] = towers[i - 1][0] + towers[i - 1][3] + towers[i - 1][5];
            } else {
                towers[i][j] = towers[i - 1][1] + towers[i - 1][2] + towers[i - 1][3] + towers[i - 1][4] + towers[i - 1][5];
            }
            towers[i][j] %= MOD;
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);
    int largest_height = 0, testcases[t];
    for (int i = 0; i < t; i++) {
        scanf("%d", &testcases[i]);
        if (testcases[i] > largest_height) {
            largest_height = testcases[i];
        }
    }

    vector<vector<long long> > towers(largest_height + 1, vector<long long>(6));
    count_towers(largest_height, towers);

    for (int i = 0; i < t; i++) {
        int ans = towers[testcases[i]][3] + towers[testcases[i]][5];
        cout << ans % MOD << endl;
    }
}