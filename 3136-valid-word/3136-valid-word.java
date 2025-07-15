class Solution {
    public boolean isValid(String s) {
        boolean v= false;
        boolean c= false;
        String vowels="aeiouAEIOU";
        String spc="@#$";
        
        if(s.length()<3){
            return false;
        }
        for ( int i=0;i<s.length();i++){
            // System.out.print(i);
            if (vowels.contains(String.valueOf(s.charAt(i))) && Character.isAlphabetic(s.charAt(i))){
                v=true;
            }
            if( Character.isAlphabetic(s.charAt(i)) &&  !vowels.contains(String.valueOf(s.charAt(i))) ){
                c=true;
            }
            if(spc.contains(String.valueOf(s.charAt(i)))){
                return false;
            }
        }
        if (v && c) return true;
        return false;
        
    }
}