// Вывод делителей числа
package main

import "fmt"

func main() {
	var num, k int
	fmt.Scan(&num)
	for i := 1; i < num+1; i++ {
		if num%i == 0 {
			k++
			fmt.Print(i, " ")
		}
	}
	if k == 2 {
		fmt.Print("\nACHTUNG")
	}
}
