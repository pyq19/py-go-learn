// Variadic functions can be called with any number of trailing arguments.
// 可变的，可变参数函数
// For example, `fmt.Println` is a common variadic function.

package main
import "fmt"

func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}
// Here's a function that will take an arbitrary(任意的,武断的) number
// of ints as arguments.

func main() {
    sum(1, 2)
    // [1 2] 3
    sum(1, 2, 3)
    // [1 2 3] 6
    // Variadic functions can be called in the usual way with 
    // individual(单独的) arguments.

    nums := []int{1, 2, 3, 4, 5}
    sum(nums...)
    // [1 2 3 4 5] 15
    // If you already have multiple args in a slice,
    // apply them to a variadic function using `func(slice...)` like this.
}
