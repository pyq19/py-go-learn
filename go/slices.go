package main

import "fmt"

func main() {
    primes := [6]int{1, 2, 3, 4, 5, 6}
    var s []int = primes[1:5] // [1:5) 2,3,4,5   5-1=4
    fmt.Println(s)
}

// [2 3 4 5]
