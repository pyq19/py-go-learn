/* The primary mechanism for managing state in Go is
communication over channels. We saw this for example
with worker pools. There are a few other options for
managing state though. Here we'll look at using the
`sync/atomic` package for atomic counters accessed by
multiple goroutines. */

package main
import "fmt"
import "time"
import "sync/atomic"

func main() {
    var ops uint64 = 0
    // we'll use an unsigned integer to represent our (always-positive) counter.

    // To simulate concurrent updates, we'll start 50 goroutines
    // that each increment the counter about once a millisecond.
    for i := 0; i < 50; i++ {
        go func() {
            for {
                atomic.AddUint64(&ops, 1)
                // To atomically increment the counter we use `AddUint64`,
                // giving it the memory address of our `ops` counter with
                // the `&` syntax.

                time.Sleep(time.Millisecond)
                // Wait a bit between increments.
            }
        }()
    }

    time.Sleep(time.Second)
    // Wait a second to allow some ops to accumulate(积累,积攒).

    opsFinal := atomic.LoadUint64(&ops)
    fmt.Println("ops:", opsFinal)// ops: 38354
    /* In order to safely use the counter while it's still being
    updated by other goroutines, we extract a copy of the current
    value into `opsFinal` via `LoadUint64`. As above we need to give
    this function the memory address `&ops` from which to fetch 
    the value. */
}

// Running the program shows that we executed about 40000 operations.

// Next we'll look at mutexes, another tool for managing state.
