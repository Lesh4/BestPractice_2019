// пирамида
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		for j := n - i; j > 1; j-- {
			fmt.Print(" ")
		}
		for k := 0; k <= (i+i)*2; k += 2 {
			fmt.Print("@")
		}
		fmt.Print("\n")
	}
}
