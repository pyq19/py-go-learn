/* We often want to execute Go code at some point in the future,
or repeatedly at some interval. Go's built-in timer and ticker
features make both of these tasks easy. We'll look first at timers
and then at tickers. */

package main
import "time"
import "fmt"

func main() {
    timer1 := time.NewTimer(time.Second * 2)
    /* Timers represent a single event in the future.
    You tell the timer how long you want to wait, and it
    provides a channel that will be notified at that time.
    This timer will wait 2 seconds. */

    <-timer1.C
    fmt.Println("Timer 1 expired")
    // The `<-timer1.C` blocks on the timer's channel `C`
    // until it sends a value indicating that the timer expired(过期).

    timer2 := time.NewTimer(time.Second)
    go func() {
        <-timer2.C
        fmt.Println("Timer 2 expired")
    }()
    stop2 := timer2.Stop()
    if stop2 {
        fmt.Println("Timer 2 stopped")
    }
    /* If you just wanted to wait, you could have used `time.Sleep`.
    One reason a timer may be useful is that you can cancel the
    timer before it expires(到期,有效期). */
}
// Timer 1 expired
// Timer 2 stopped

// The first timer will expire ~2s after we start the program,
// but the second should be stopped before it has a chance to expire(期满,死亡).
