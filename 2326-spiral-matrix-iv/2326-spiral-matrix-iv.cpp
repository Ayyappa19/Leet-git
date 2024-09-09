/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> ans(m, vector<int>(n, -1));
        int e = 0, f = m - 1, g = 0, h = n - 1;
        while (head) {
            int i = g;
            while (i <= h && head) {
                ans[e][i] = head->val;
                head = head->next;
                i++;
            }
            e++;
            i = e;
            while (i <= f && head) {
                ans[i][h] = head->val;
                head = head->next;
                i++;
            }
            h--;
            i = h;
            while (i >= g && head) {
                ans[f][i] = head->val;
                head = head->next;
                i--;
            }
            f--;
            i = f;
            while (i >= e && head) {
                ans[i][g] = head->val;
                head = head->next;
                i--;
            }
            g++;
        }
        return ans;
    }
};