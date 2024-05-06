class FindThePrefixCommonArrayOfTwoArrays {
    public static int[] findThePrefixCommonArray(int[] A, int[] B) {
        int bitSetLen = Arrays.stream(A).max().getAsInt() + 1;
        BitSet bitSetA = new BitSet(bitSetLen);
        BitSet bitSetB = new BitSet(bitSetLen);
        BitSet bitSetC;
        int[] C = new int[A.length];
        for (int i = 0; i < A.length; i++){
            bitSetA.set(A[i]);
            bitSetB.set(B[i]);
            bitSetC = (BitSet)bitSetA.clone();
            bitSetC.and(bitSetB);
            C[i] = bitSetC.cardinality();
        }
        return C;
    }
}