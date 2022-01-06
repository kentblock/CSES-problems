#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

const int MOD = pow(10, 9) + 7;

long long num_descriptions(vector<int> arr, int upper_bound) {

    vector<long long> prev(upper_bound + 2);
    vector<long long> cur(upper_bound + 2);

    if (arr[0]) {
        prev[arr[0]] = 1;
    } else {
        for (int i = 1; i < upper_bound + 1; i++) {
            prev[i] = 1;
        }
    }

    for (int i = 1; i < arr.size(); i++) {
        if (arr[i]) {
            cur[arr[i]] = prev[arr[i]] + prev[arr[i] - 1] + prev[arr[i] + 1];
            cur[arr[i]] %= MOD;
        } else {
            for (int j = 1; j <= upper_bound; j++) {
                cur[j] = prev[j] + prev[j - 1] + prev[j + 1];
                cur[j] %= MOD;
            }
        }
        prev = cur;
        cur = vector<long long>(upper_bound + 2);
    }
    long long init = 0;
    return accumulate(prev.begin(), prev.end(), init) % MOD;
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
    int upper_bound = read_num();
    vector<int> arr = read_nums(size);
    cout << num_descriptions(arr, upper_bound) << endl;
}