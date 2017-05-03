// Go supports recursive functions.
// Here's a classic factorial(因子的,阶乘的) example.

package main
import "fmt"

func fact(n int) int {
    if n == 0 {
        return 1
    }
    return n * fact(n-1)
}
// This `fact` function calls itself until it reaches the
// base case of `fact(0)`.

func main() {
    fmt.Println(fact(7))// 5040
}
