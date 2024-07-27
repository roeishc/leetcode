class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        res = []
        sorted_products = deepcopy(products)
        sorted_products.sort()

        left, right = 0, len(products) - 1

        for i, c in enumerate(searchWord):
            
            while left <= right and (len(sorted_products[left]) <= i or sorted_products[left][i] != c):
                left += 1
            while left <= right and (len(sorted_products[right]) <= i or sorted_products[right][i] != c):
                right -= 1
            
            res.append([])
            for j in range(min(3, right - left + 1)):   # add up to 3 matching words
                res[-1].append(sorted_products[left + j])
        
        return res

        
        # initial solution: brute force

        # sorted_products = deepcopy(products)
        # sorted_products.sort()

        # res = []
        # for i in range(len(searchWord)):
        #     suggestions = []
        #     for product in sorted_products:
        #         if product.startswith(searchWord[:i+1]):
        #             suggestions.append(product)
        #         if len(suggestions) == 3:
        #             break
        #     res.append(suggestions)

        # return res
