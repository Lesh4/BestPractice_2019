//Необычные шахматы от BPS
package main

import "fmt"

func main() {
	var col_1, str_1, col_2, str_2 int
	fmt.Scan(&col_1)
	fmt.Scan(&str_1)
	fmt.Scan(&col_2)
	fmt.Scan(&str_2)
	if (col_1+2 == col_2 && str_1+5 == str_2) || (col_1+5 == col_2 && str_1+2 == str_2) {
		fmt.Print("YESSSS!")
	} else if (col_2+2 == col_1 && str_2+5 == str_1) || (col_2+5 == col_1 && str_2+2 == str_1) {
		fmt.Print("YESSSS!")
	} else {
		fmt.Print("No no")
	}
}
