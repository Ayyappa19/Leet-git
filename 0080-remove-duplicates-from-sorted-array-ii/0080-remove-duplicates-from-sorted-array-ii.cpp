class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=2,j=2;
        // 0 0 1 1 1 1 2 3 3
        //           i
        //               j
        if(nums.size()==0)return 0;
        if(nums.size()<=2){
            return nums.size();
        }
        while(j<nums.size()){
            if (nums[j]!=nums[i-2]){
                // cout<<nums[j]<<nums[i-2]<<endl;
                
                nums[i]=nums[j];
                cout<<nums[i];
                i++;
            }
            j++;
        }
        return i;
    }
};