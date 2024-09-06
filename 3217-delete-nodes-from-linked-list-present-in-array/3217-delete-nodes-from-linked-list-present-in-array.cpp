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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int>l(nums.begin(),nums.end());
        ListNode temp(0);

        temp.next=head;
        ListNode* cur=&temp;
        while(cur->next!=NULL){

            if(l.find(cur->next->val)!=l.end()){
                ListNode* del=cur->next;
                cur->next=cur->next->next;
            }
            else{
                cur=cur->next;
            }
        }
        return temp.next;
        
    }
};
