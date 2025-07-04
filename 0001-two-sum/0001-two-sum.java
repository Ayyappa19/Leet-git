class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> d= new HashMap<>();
        int n= nums.length;
        for ( int i =0;i<n;i++){
            int k= target-nums[i];
            if (d.containsKey(k)){
                return new int[]{i,d.get(k)};
            }
            else{
                d.put(nums[i],i);
            }
        }
        return new int []{};
        
    }
}