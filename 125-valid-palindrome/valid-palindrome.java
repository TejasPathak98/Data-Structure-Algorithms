class Solution 
{
    public boolean isPalindrome(String s) 
    {
        if(s.length() == 0)
        {
            return true;
        }

        int start = 0;
        int last = s.length() - 1;

        while(start <= last) 
        {
            if(!Character.isLetterOrDigit(s.charAt(start)))
            {
                start++;
            }
            else if(!Character.isLetterOrDigit(s.charAt(last)))
            {
                last--;
            }
            else 
            {

                char st = s.charAt(start);
                char l = s.charAt(last);
                if(Character.toLowerCase(st) != Character.toLowerCase(l))
                {
                    return false;
                }
                start++;
                last--;
            }
        }
        return true;

    }
}