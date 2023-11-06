package main

import (
	"fmt"
	"strconv"
)

func main() {
	var l, r int
	fmt.Scanf("%d %d", &l, &r)

	var count int = 0
	for i := l; i <= r; i++ {
		if IsKaibun(i) {
			count ++
		}
	}

	fmt.Println(count)
}

func IsKaibun(input int) bool {
	str := strconv.Itoa(input)
	result := true
	len := len(str)

	for i := 0; i <= len / 2; i++ {
		if str[i] != str[len-i-1] {
			result = false
		}
	}

	return result
}