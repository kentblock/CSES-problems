#include <iostream>
#include <vector>
using namespace std;

const int MAX_RIDES = 20;

// TODO refactor, pretty messy
// Intuition: compute min # rides and the weight of the last ride for every subset of weights
int min_elevator_rides(vector<int> weights, int max_weight, int n) {

    vector<int> min_rides(1 << n, MAX_RIDES + 1);
    vector<int> min_last_weight(1 << n, max_weight + 1);
    min_rides[0] = 1;
    min_last_weight[0] = 0;
    for (int i = 1; i < 1 << n; i++) {
        for (int j = 0; j < n; j++) {
            if (i & 1 << j) {
                int subset = i ^ (1 << j);
                int num_rides = min_rides[subset];
                int ride_weight = min_last_weight[subset];
                int new_ride_weight;
                if (ride_weight + weights[j] <= max_weight) {
                    new_ride_weight = ride_weight + weights[j];
                } else {
                    new_ride_weight = weights[j];
                    num_rides += 1;
                }
                if (num_rides < min_rides[i]) {
                    min_rides[i] = num_rides;
                    min_last_weight[i] = new_ride_weight;

                } else if (num_rides == min_rides[i]) {
                    min_last_weight[i] = min(min_last_weight[i], new_ride_weight);
                }
            }
        }
    }
    return min_rides[(1 << n) - 1];
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

    int n = read_num();
    int max_weight = read_num();
    vector<int> weights = read_nums(n);

    cout << min_elevator_rides(weights, max_weight, n) << endl;
}