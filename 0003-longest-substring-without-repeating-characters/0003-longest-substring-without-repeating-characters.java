class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> mp= new HashMap<>();
        int maxi=0;
        int j=0;
        for (int i=0;i<s.length();i++){
            if(mp.containsKey(s.charAt(i))){
                j=mp.get(s.charAt(i))+1;
                String ss=s.substring(j,i+1);
                // System.out.println(ss);
                maxi=Math.max(maxi,ss.length());
                mp.put(s.charAt(i),i);


            }
            else{
                mp.put(s.charAt(i),i);
                String ss=s.substring(j,i+1);
                maxi=Math.max(maxi,ss.length());
            }
        }
        return maxi;
        
    }
}