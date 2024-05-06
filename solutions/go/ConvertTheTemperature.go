func convertTemperature(celsius float64) []float64 {

	ans := make([]float64, 2)
	ans[0] = celsius + 273.15
	ans[1] = celsius*1.8 + 32

	return ans

}