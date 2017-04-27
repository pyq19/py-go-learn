package main

import "fmt"

func main() {
    var a [2]string
    a[0] = "hello"
    a[1] = "world"
    fmt.Println(a[0], a[1])
    fmt.Println(a)

    primes := [6]int{1, 3, 5, 7, 9}
    fmt.Println(primes)
}

// hello world
// [hello world]
// [1 3 5 7 9 0]
