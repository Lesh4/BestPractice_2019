// Числа фибоначчи
package main

import "fmt"

func fib(n int) int {
	var a, b int = 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	return a
}

func main() {
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		if i+1 != n {
			fmt.Printf("%d, ", fib(i))
		} else {
			fmt.Printf("%d ", fib(i))
		}
	}
}
