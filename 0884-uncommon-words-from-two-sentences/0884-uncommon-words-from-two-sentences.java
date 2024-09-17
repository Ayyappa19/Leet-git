class Solution {
    HashMap<String, Integer> m= new HashMap<>();
    void hashConvertor(String[] s1){
        for( int i=0;i<s1.length;i++){
            if (m.containsKey(s1[i])){
                m.put(s1[i],m.get(s1[i])+1);
            }
            else{
                m.put(s1[i],1);
            }
        }
    }
    public String[] uncommonFromSentences(String s1, String s2) {
        String [] s=s1.split(" ",0);
        String [] ss=s2.split(" ",0);
        
        hashConvertor(s);
        hashConvertor(ss);
        
        ArrayList<String>v=new ArrayList<String>();
        for(Map.Entry<String,Integer> i:m.entrySet()){
            if(i.getValue()==1){
                v.add(i.getKey());
            }
        }
        String[] aa =new String[v.size()];
        int j=0;
        for(String i:v){
            aa[j]=i;
            j++;
        }
        return aa;

        
        
    }
}