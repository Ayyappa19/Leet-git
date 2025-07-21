class Solution {
    public String convert(String s, int n) {
        if(n>=s.length() || n==1) return s;


        StringBuilder res= new StringBuilder();
        for( int i =0;i<n;i++){
            int nrml=(n*2)-2;
            int diag=i;


            for( int j=0;j<s.length();j=j+nrml){
                if(i+j <s.length())
                res.append(s.charAt(i+j));


                if(i!=0 && i!=n-1 && (j+nrml-diag)<s.length()){
                    res.append(s.charAt((j+nrml)-diag));
                }
            }

        }
        return res.toString();
        
    }
}