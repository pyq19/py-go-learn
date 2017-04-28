// http://stackoverflow.com/questions/16466320/is-there-a-way-to-do-repetitive-tasks-at-intervals-in-golang
// Is there a way to do repetitive(重复的) tasks at intervals in Golang?

// I know I can do this with a goroutine and `Time.sleep()`
// but I'd like something that easily stopped.
// Here's what I got, but looks ugly to me. Is there a cleaner/better way?
/*
func oneWay() {
    var f func()
    var t *time.Timer

    f = func() {
        fmt.Println("doing stuff")
        t = time.AfterFunc(time.Duration(5) * time.Second, f)
    }
    t = time.AfterFunc(time.Duration(5) * time.Second, f)
    defer t.Stop()

    // simulate doing stuff
    time.Sleep(time.Minute)
}
*/
//////////////
/*
// The function `time.NewTicker` makes a channel that sends a periodic(周期的，定期的) message,
// and provides a way to stop if. Use it something like this:
ticker := time.NewTicker(5 * time.Second)
quit := make(chan struct{})
go func() {
    for {
        select {
        case <- ticker.C:
            // do stuff
        case <- quit:
            ticker.Stop()
            return
        }
    }
}()
// You can stop the worker by closing the `quit` channer: `close(quit)`
*/
///////////////////
/*
package main
import (
    "fmt"
    "time"
)
func schedule(what func(), delay time.Duration) chan bool {
    stop := make(chan bool)

    go func() {
        for {
            what()
            select {
            case <-time.After(delay):
            case <-stop:
                return
            }
        }
    }()
    return stop
}
func main() {
    ping := func() {fmt.Println("#")}

    stop := schedule(ping, 5 * time.Millisecond)
    time.Sleep(25 * time.Millisecond)
    stop <- true
    time.Sleep(25 * time.Millisecond)

    fmt.Println("done")
}
// #
// #
// #
// #
// #
// done
*/
//////////////////////

// If you do not care about tick shifting (depending on how long did it took previously on each execution)
// and you do not want to use channels, it's possible to use native range function.
package main
import "fmt"
import "time"
func main() {
    go heartBeat()
    time.Sleep(time.Second * 5)
}
func heartBeat() {
    for range time.Tick(time.Second * 1) {
        fmt.Println("Foo")
    }
}
// Foo
// Foo
// Foo
// Foo
// Foo
