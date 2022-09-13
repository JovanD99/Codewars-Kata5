public static int TrailingZeros(int n)
  {
    int zeros = 0;
    while (true)
    {
        zeros += (n/5);
        n /= 5;
        if (n == 0)
            break;
    }
        
    return zeros;
  }
