package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	root := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 7,
			Left: &TreeNode{
				Val: 7,
			},
			Right: &TreeNode{
				Val: -8,
			},
		},
		Right: &TreeNode{
			Val: 0,
		},
	}

	fmt.Println(maxLevelSum(&root))
}

func maxLevelSum(root *TreeNode) int {
	levelSums := make(map[int]int)
	traverseTree(root, 1, levelSums)

	maxSum := math.Inf(-1)
	maxDepth := math.Inf(-1)

	for k, v := range levelSums {
		if v > int(maxSum) {
			maxSum = float64(v)
			maxDepth = float64(k)
		}
	}

	return int(maxDepth)
}

func traverseTree(node *TreeNode, depth int, levelSums map[int]int) {
	levelSums[depth] += node.Val

	if node.Left != nil {
		traverseTree(node.Left, depth+1, levelSums)
	}
	if node.Right != nil {
		traverseTree(node.Right, depth+1, levelSums)
	}
}
