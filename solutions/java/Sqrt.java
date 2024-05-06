class Sqrt {
    public int mySqrt(int x) {
        if (x == 1)
            return 1;
        int start = 1, end = x, mid;
        while (start < end) {
            mid = start + (end - start) / 2;
            if (mid <= x / mid) // to keep from overflowing, don't use mid*mid
                start = mid + 1;
            else
                end = mid;
        }
        return start - 1;
    }
}