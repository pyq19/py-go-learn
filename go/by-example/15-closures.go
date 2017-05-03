// Go supports anonymous functions, which can form closures(闭包).
// Anonymous functions are useful when you want to define a function
// inline without having to name it.

package main
import "fmt"

func intSeq() func() int {
    i := 0
    return func() int {
        i += 1
        return i
    }
}
// This function `intSeq` returns another function,
// which we define anonymously in the body of `intSeq`.
// The returned function closes over the variable `i`
// to form a closure.

func main() {
    nextInt := intSeq()
    /* We call `intSeq`, assigning(分派,设定) the result (a function)
    to `nextInt`. This function value captures(捕获,夺得) its own `i` value,
    which will be updated each time we call `nextInt`. */

    fmt.Println(nextInt())
    fmt.Println(nextInt())
    fmt.Println(nextInt())
    // See the effect of the closure by calling `nextInt` a few times.

    newInts := intSeq()
    fmt.Println(newInts())
    // To confirm that the state is unique to that particular(特别的,详细的)
    // function, create and test a new one.
}
// 1
// 2
// 3
// 1
