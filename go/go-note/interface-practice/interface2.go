package main

import "fmt"

func Print(v interface{}) {
    fmt.Printf("%T: %v\n", v, v)
}

func main() {
    Print(1)
    Print("hello world....")
}

// int: 1
// string: hello world....
