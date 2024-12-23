/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode  temp=head,dum=head;
        int c=0;
        while(dum!=null){
            c+=1;
            dum=dum.next;
        }
        if(c==1){
            return null;
        }
        else if (c==n){
            head=head.next;
            temp.next=null;
            return head;
            
        }
        int k=c-n;
        while(k>1){
            temp=temp.next;
            k-=1;
        }
            ListNode  temp2=temp.next;
            temp2=temp2.next;
            temp.next=temp2;
            return head;
    }
}