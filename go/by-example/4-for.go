// `for` is Go's only looping construct.

package main
import "fmt"

func main() {
    i := 1
    for i <= 3 {
        fmt.Println(i)
        i = i + 1
    }
    // 1 2 3
    // The most basic type, with a single condition.

    for j := 7; j <= 9; j++ {
        fmt.Println(j)
    }
    // 7 8 9
    // A classic initial/condition/after `for` loop.

    for {
        fmt.Println("loop")
        break
    }
    // loop
    // `for` without a condition will loop repeatedly
    // until you break out of the loop or `return` from the enclosing function.

    for n := 0; n <= 5; n++ {
        if n%2 == 0 {
            continue
        }
        fmt.Println(n)
    }
    // 1 3 5
    // You can also `continue` to the next iteration of the loop.
}

// We'll see some other `for` forms later when
// we look at `range` statements, channels, and other data structures.
