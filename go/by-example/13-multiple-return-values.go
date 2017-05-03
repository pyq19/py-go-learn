// Go has built-in support for multiple return values.
// This feature is used often in idiomatic(惯用的,符合语言习惯的) Go,
// e.g. to return both result and error values from a function.

package main
import "fmt"

func vals() (int, int) {
    return 3, 7
}

func main() {
    a, b := vals()
    fmt.Println(a) // 3
    fmt.Println(b) // 7

    _, c := vals()
    fmt.Println(c) // 7
}
