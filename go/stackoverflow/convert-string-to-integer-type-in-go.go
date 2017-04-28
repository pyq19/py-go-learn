// http://stackoverflow.com/questions/4278430/convert-string-to-integer-type-in-go

// Convert string to integer type in Go?
// I'm trying to convert a string returned from `flag.Arg(n)` to an `int`.
// What is the idiomatic way to do this in Go?

///////////////////////////

package main
import (
    "flag"
    "fmt"
    "os"
    "strconv"
)
func main() {
    flag.Parse()
    s := flag.Arg(0)
    // string to int
    i, err := strconv.Atoi(s)
    if err != nil {
        // handle error
        fmt.Println(err)
        os.Exit(2)
    }
    fmt.Println(s, i)
}
// go: unknown subcommand "cun"
// Run 'go help' for usage.
