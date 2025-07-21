class Solution {
    public static final int infi=0x3f3f3f3f;

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int [] curr=new int[n];
        int [] prev= new int[n];
        Arrays.fill(curr, infi);
        curr[src]=0;
        for( int i=0;i<k+1;i++){

            System.arraycopy(curr, 0, prev,0,n);

            for(int [] arr: flights){
                int from =arr[0], to= arr[1] , cost=arr[2];
                curr[to]= Math.min(curr[to], prev[from]+cost);
            }


        }
        return curr[dst]==infi ?-1: curr[dst];
        
    }
}