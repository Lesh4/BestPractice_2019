package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strings"
)

func Scan1() string {
	in := bufio.NewReader(os.Stdin)
	str, err := in.ReadString('\n')
	if err != nil {
		fmt.Println("Ошибка ввода: ", err)
	}
	return str
}

func main() {
	var re = regexp.MustCompile(`[[:punct:]]|[[:space:]]|[A-Z]+=`)
	var STR string
	dict := map[string]int{}
	STR = Scan1()
	strings.Replace(STR, " ", "", -1)
	NEW_WORDS := re.ReplaceAllString(STR, "")
	NEW_WORDS = strings.ToLower(NEW_WORDS)
	for i := 0; i < len(NEW_WORDS); i++ {
		if dict[string(NEW_WORDS[i])] == 0 {
			dict[string(NEW_WORDS[i])] = 1
		} else {
			dict[string(NEW_WORDS[i])] += 1
		}
	}

	type kv struct {
		Key   string
		Value int
	}

	var ss []kv
	for k, v := range dict {
		ss = append(ss, kv{k, v})
	}

	sort.Slice(ss, func(i, j int) bool {
		return ss[i].Value > ss[j].Value
	})

	sort.Slice(ss, func(i, j int) bool {
		if ss[i].Value == ss[j].Value {
			return ss[i].Key < ss[j].Key
		} else {
			return ss[i].Value > ss[j].Value
		}
	})

	for _, kv := range ss {
		fmt.Printf("%s: %d\n", kv.Key, kv.Value)
	}
}
