// Условие: На вход программе попадает число A ( > 0).
// Необходимо подсчитать сумму двух БЛИЖАЙШИХ (el1 >= A >= el2, el1+ el2, где el1 и el2 элементы последовательности Фибоначи)
// к этому числу элементов последовательности Фибоначи.
package main

import "fmt"

func fib(n int) int {
	var a, b int = 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	return a
}

func make_mas(n int) []int {
	var mas []int
	mas = make([]int, n)
	for i := 0; i < n; i++ {
		mas[i] = fib(i)
	}
	return mas[:]
}

func main() {
	var num, res, kol int
	var mas []int
	fmt.Scan(&num)
	kol = 1
LOOP:
	for {
		mas = make_mas(kol)
		for i := 0; i < kol; i++ {
			if num < mas[i] {
				break LOOP
			}
		}
		kol++
	}

	for i := 0; i < kol; i++ {
		if num > mas[i] {
			res = mas[i] + mas[i+1]
		}
	}
	fmt.Print(res)
}
