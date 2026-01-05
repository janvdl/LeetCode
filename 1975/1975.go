package main

import (
	"fmt"
	"math"
)

func main() {
	var matrix [][]int = [][]int{
		{1, 2, 3},
		{-1, -2, -3},
		{1, 2, 3},
	}
	fmt.Println(maxMatrixSum(matrix))

	matrix = [][]int{
		{1, -1},
		{-1, 1},
	}
	fmt.Println(maxMatrixSum(matrix))
}

func maxMatrixSum(matrix [][]int) int64 {
	// i had to peek at the hints and discussion
	// for this one to get the trick.

	// by chaining pairs of cells together, you can
	// convert any cell from negative to positive.

	// if there are an even number of negatives in the
	// matrix, all values can be converted to positive.
	// if there are an odd number of negatives in the
	// matrix, one value must remain negative.
	// this can be the smallest value in the matrix to
	// maximise the value returned.
	smallest_val := math.Inf(1)
	matrix_sum := 0
	neg_count := 0

	for x := range matrix {
		for y := range matrix[0] {
			val := matrix[x][y]
			if val < 0 {
				neg_count++
			}

			abs_val := math.Abs(float64(val))
			if abs_val < smallest_val {
				smallest_val = abs_val
			}

			matrix_sum += int(abs_val)
		}
	}

	if math.Mod(float64(neg_count), 2) == 0 {
		return int64(matrix_sum)
	} else {
		return int64(matrix_sum) - (int64(smallest_val) * 2)
	}
}
