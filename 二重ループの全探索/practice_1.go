package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
    // input
    var n int

	fmt.Scanf("%d", &n)

    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    inputs := strings.Split(sc.Text(), " ")

    var A [] int

    for _, input := range inputs {
		a, _ := strconv.Atoi(input) 
		A = append(A, a) 
    }
    
    // process
    var count int = 0 
    for _, a := range A {
        if isPrime(a) {
            count ++
        }
    }

    // output
    fmt.Print(count)
}

func isPrime(input int) bool {
    var count int = 1
    var result bool = false
    for number := 2; number <= input; number++ {
        if input % number == 0 {
            count ++
        }
        if count >= 3 {
            break
        }
    }

    // 約数が２つのみに限り、素数判定とする。
    if count == 2 {
        result = true
    }

    return result
}