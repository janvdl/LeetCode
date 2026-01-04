package main

import (
	"fmt"
	"math"
	"slices"
)

func main() {
	bla := sumFourDivisors([]int{21, 4, 7})
	fmt.Println(bla)
}

func sumFourDivisors(nums []int) int {
	divisor_total := 0

	for _, num := range nums {
		max := int(math.Floor(math.Sqrt(float64(num)))) + 1
		known_divisors := []int{}

		for divisor := range max {
			if math.Mod(float64(num), float64(divisor)) == 0 {
				divisor_counterpart := num / divisor

				if !slices.Contains(known_divisors, divisor) {
					known_divisors = append(known_divisors, divisor)
				}
				if !slices.Contains(known_divisors, divisor_counterpart) {
					known_divisors = append(known_divisors, divisor_counterpart)
				}
			}

			if len(known_divisors) > 4 {
				break
			}
		}

		if len(known_divisors) == 4 {
			for _, x := range known_divisors {
				divisor_total += x
			}
		}
	}

	return divisor_total
}
