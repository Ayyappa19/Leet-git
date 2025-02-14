class Solution {
public:
    int search(vector<int>& nums, int target) {
        // 0 1 2 3 4 5 6
        // 4 5 6 7 0 1 2    t=0
        // i
        //             j
        int i=0,j=nums.size()-1;
        while(i<=j){
            int mid=(i+j)/2;
            if(nums[mid]==target)return mid;
            if(nums[i]<=nums[mid]){
                if(nums[i]<=target and nums[mid]>target){
                    j=mid-1;
                }
                else{
                    i=mid+1;
                }
            }
            else{
                if(nums[mid]<target and nums[j]>=target){
                    i=mid+1;
                }
                else{
                    j=mid-1;
                }
            }
        }
        return -1;



    }
};