// http://stackoverflow.com/questions/11268943/golang-is-it-possible-to-capture-a-ctrlc-signal-and-run-a-cleanup-function-in

// I want to capture the `Ctrl+C` (SIGINT) signal sent from the console and print out some partial run totals.
// Is this possible in Golang?
// Note: When I first posted the question I was confused about `Ctrl+C` being `SIGTERM` instead of `SIGINT`.

///////////////////////
/*
// You can use the `os/signal` package to handle incoming signals.
// ^C is `SIGINT`, so you can use this to trap `os.Interrupt`.
c := make(chan os.Signal, 1)
signal.Notify(c, os.Interrupt)
go func(){
    for sig := range c {
        // sig is a ^C, handle it
    }
}()
// The manner in which you cause your program to terminate and print information
// is entirely up to you.
*/
/////////////////////////

package main
import (
    "fmt"
    "os"
    "os/signal"
    "syscall"
    "time"  // or "runtime"
)
func cleanup() {
    fmt.Println("cleanup")
}
func main() {
    c := make(chan os.Signal, 2)
    signal.Notify(c, os.Interrupt, syscall.SIGTERM)
    go func() {
        <-c
        cleanup()
        os.Exit(1)
    }()

    for {
        fmt.Println("sleeping......")
        time.Sleep(10 * time.Second)    // or runtime.Gosched() or similar per @misterbee
    }
}
// sleeping......
// ^Ccleanup
// exit status 1
