func numIdenticalPairs(nums []int) int {

	count := make(map[int]int)

	for _, val := range nums {
		count[val]++
	}

	total := 0
	for _, val := range count {
		total += val * (val - 1) / 2
	}

	return total

}
