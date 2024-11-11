class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def is_prime(num):
            for n in range(2, int(sqrt(num)) + 1):
                if num % n == 0:
                    return False
            return True
        
        primes = [0, 0]
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i - 1])
            
        prev = 0
        for n in nums:
            upper_bound = n - prev
            largest_prime = primes[upper_bound - 1]
            if n - largest_prime <= prev:
                return False
            prev = n - largest_prime

        return True
