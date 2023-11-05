package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scanf("%d %d", &n, &k)

	var A [] int

	for i := 1; i <= n; i++ {
		var count int = 0
		for j := 1; j <= i; j++ {
			if i % j == 0 {
				count ++
			}
		}

		if count == k {
			A = append(A, i)
		}
	}

	fmt.Print(len(A))
}