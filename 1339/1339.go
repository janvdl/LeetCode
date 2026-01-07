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
	/*
	* 	My logic is the following:
	*
	*	Each tree has a total sum of its nodes, say S.
	* 	By selecting any child node and calculating the sum of the nodes
	* 	of the subtree, we get sum s1 and can derive the sum of the 2nd subtree
	* 	as s2 = S - s1.
	*
	*	The product is then s1 * s2 and once the maximum product is found it can be returned.
	 */

	root := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 4,
			},
			Right: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 6,
			},
		},
	}

	fmt.Println(maxProduct(&root))
}

func maxProduct(root *TreeNode) int {
	// keep track of subtree sums
	sumLookup := make(map[*TreeNode]int)

	//queue of nodes to check
	q := []*TreeNode{}
	q = append(q, root.Left)
	q = append(q, root.Right)

	// work through the nodes and add children as they are discovered
	for len(q) > 0 {
		// get the last item added and pop it from the queue
		// update the length of the queue
		l := len(q)
		n := q[l-1]
		q = q[:l-1]

		if n == nil {
			continue
		} else {
			treeSum(n, sumLookup) // get sum of subtree starting from this node
			q = append(q, n.Left)
			q = append(q, n.Right)
		}
	}

	// the hashmap has been populated with the subtree sums
	// now find max product
	totalTreeSum := treeSum(root, sumLookup)
	max := 0
	for _, v := range sumLookup {
		s1 := v
		s2 := totalTreeSum - s1
		tmp := s1 * s2
		if tmp > max {
			max = tmp
		}
	}

	// mod the answer as requested by the problem statement
	modulo := math.Pow(10, 9) + 7
	max = int(math.Mod(float64(max), modulo))

	return max
}

// with memoisation via hashmap sumLookup
func treeSum(node *TreeNode, sumLookup map[*TreeNode]int) int {
	if node == nil {
		return 0
	} else {
		if val, ok := sumLookup[node]; ok {
			return val
		} else {
			sumLookup[node] = node.Val + treeSum(node.Left, sumLookup) + treeSum(node.Right, sumLookup)
			return sumLookup[node]
		}

	}
}
