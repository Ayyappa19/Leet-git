class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int[] a = new int[spells.length];
        Arrays.fill(a,0);
        for(int i = 0 ; i < potions.length ; i++)
        {
            int f = 0 ;
            int l = spells.length - 1;
            while(f < l)
            {
                int p = spells[f]*potions[i];
                int lp = spells[l]*potions[i];
                if(p>=success)
                a[f]+=1;
                if(lp>=success)
                a[l]+=1;
                f++;
                l--;
            }
            if(f==l)
            {
                int p = spells[f]*potions[i];
                if(p>=success)
                a[f]+=1;
            }
        }
        return a;
    }
}