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
    int gcd(int a,int b){
        int ans = min(a, b);
        while (ans > 0) {
            if (a % ans == 0 && b % ans == 0) {
                break;
            }
            ans--;
        }
    return ans;

    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode *dum1=head ,*dum2=head->next;
        while(dum2!=NULL){
            int k=gcd(dum1->val,dum2->val);
            ListNode *temp=new ListNode(k);
            dum1->next=temp;
            temp->next=dum2;
            dum1=dum2;
            dum2=dum2->next;
        }

        return head;
    }
};