class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int c = prices[0];
        int p = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < c) {
                c = prices[i];
            } else if (prices[i] - c > p) {
                p = prices[i] - c;
            }
        }
        return p;
    }
};