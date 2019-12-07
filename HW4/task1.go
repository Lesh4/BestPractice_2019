// Подсчет количества денег на отправку тектового сообщения
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var coast int = 0
	myscanner := bufio.NewScanner(os.Stdin)
	myscanner.Scan()
	str := myscanner.Text()
	fmt.Println(len([]rune(str)))
	for i := 0; i < len([]rune(str)); i++ {
		coast += 23
	}
	fmt.Print(coast/100, " р. ", coast%100, " коп.")
}
