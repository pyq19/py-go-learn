// A goroutine is a lightweight thread of execution.

package main
import "fmt"

func f(from string) {
    for i := 0; i < 3; i++ {
        fmt.Println(from, ":", i)
    }
}

func main() {
    f("direct")
    // Suppose we have a function call `f(s)`.
    // Here's how we'd call that in the usual way,
    // running it synchronously(同步地).

    go f("goroutine")
    // To invoke this function in a goroutine,
    // use `go f(s)`. This new goroutine will execute
    // concurrently with the calling one.

    go func(msg string) {
        fmt.Println(msg)
    }("going")
    // You can also start a goroutine for an anonymous function call.

    var input string
    fmt.Scanln(&input)
    fmt.Println("done")
    /* Our two function calls are running asynchronously in
    separate goroutines now, so execution falls through to here.
    This `Scanln` code requires we press a key before the program exits. */
}
// direct : 0
// direct : 1
// direct : 2
// goroutine : 0
// goroutine : 1
// goroutine : 2
// going
// ==========
// done
/* When we run this program, we see the output of the blocking
call first, then the interleaved output of the two goroutines.
This interleaving reflects the goroutines being run concurrently
by the Go runtime. */
