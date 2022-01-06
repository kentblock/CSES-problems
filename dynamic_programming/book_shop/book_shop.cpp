#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Knapsack problem (good to review)
int max_pages(vector<int> prices, vector<int> pages, int max_price) {
    vector<int> dp(max_price + 1);
    for (int i = 0; i < prices.size(); i++) {
        int price = prices[i];
        for (int j = max_price - price; j >= 0; j--) {
            dp[j + price] = max(
                dp[j + price], dp[j] + pages[i]
            );
        }
    }
    return dp[max_price];
}

vector<int> read_nums(int size) {
    vector<int> nums(size);
    for (int i = 0; i < size; i++) {
        int num;
        scanf("%d", &num);
        nums.push_back(num);
    }
    return nums;
}

int read_num() {
    int num;
    scanf("%d", &num);
    return num;
}

int main() {
    int num_books = read_num();
    int max_price = read_num();
    vector<int> prices = read_nums(num_books);
    vector<int> pages = read_nums(num_books);

    cout << max_pages(prices, pages, max_price) << endl;
}