/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *temp=head,*a=head,*b=head;
            while(b != NULL && b->next!=NULL){ 
                a=a->next;
                b=b->next->next;
                if (a==b){
                    return true;
                }
            }
            return false;

        
    }
};