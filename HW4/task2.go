// Калькулятор с предвидением ошибок
package main

import "fmt"

func main() {
	var a, b float64
	var sim string
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&sim)
	if sim == "+" {
		fmt.Printf("%.2f", a+b)
	} else if sim == "-" {
		fmt.Printf("%.2f", a-b)
	} else if sim == "/" {
		if b == 0 {
			fmt.Print("ЫЫЫЫЫЫ")
		} else {
			fmt.Printf("%.2f", a/b)
		}
	} else if sim == "*" {
		fmt.Printf("%.2f", a*b)
	} else {
		fmt.Print("ЫЫЫЫЫЫ")
	}
}
