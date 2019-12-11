//Королевы бьют друг друга
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func index(list []string, a string, n int) int {
	for i := 0; i < n; i++ {
		if list[i] == a {
			return i
		}
	}
	return 0
}

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func plus_check(str []string, colums []string) bool {
	for i := 0; i < 8-1; i++ {
		for j := i; j < 8-1; j++ {
			if str[i] == str[j+1] || colums[i] == colums[j+1] {
				return true
			}
		}
	}
	return false
}

func diag_check(str []string, colums []string, flag int) bool {
	var f_func bool
	var znach_sr, k int
	f_func = false
	for i := 0; i < 8; i++ {
		znach, _ := strconv.Atoi(colums[i])
		if znach == 1 {
			elem, _ := strconv.Atoi(str[i])
			k = 8 - elem
			znach = 2
		} else {
			for znach != 1 {
				znach -= 1
				k++
			}

		}
		fin := k
		for j := 0; j < fin; j++ {
			if stringInSlice(strconv.Itoa(znach), colums[:]) {
				index1 := index(colums[:], strconv.Itoa(znach), 8)
				if flag == 1 {
					elem, _ := strconv.Atoi(str[i])
					znach_sr = elem + k
				} else {
					elem, _ := strconv.Atoi(str[i])
					znach_sr = elem - k
				}
				if stringInSlice(strconv.Itoa(znach_sr), str[:]) {
					index2 := index(str[:], strconv.Itoa(znach_sr), 8)
					if index1 == index2 {
						f_func = true
					}
				}
			}
			znach += 1
			k -= 1
		}
	}
	return f_func
}

func main() {
	var s string
	var str [8]string
	var colums [8]string
	for i := 0; i < 8; i++ {
		myscanner := bufio.NewScanner(os.Stdin)
		myscanner.Scan()
		s = myscanner.Text()
		coord := strings.Split(s, " ")
		colums[i] = coord[0]
		str[i] = coord[1]
	}
	fmt.Println(colums)
	fmt.Println(str)

	f_plus := plus_check(str[:], colums[:])
	f_diag_g := diag_check(str[:], colums[:], 1)
	f_diag_p := diag_check(str[:], colums[:], 2)
	if f_plus || f_diag_g || f_diag_p == true {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
