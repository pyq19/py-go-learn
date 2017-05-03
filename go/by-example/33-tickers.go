/* Timers are for when you want to do something once
in the future - tickers are for when you want to do something 
repeatedly at regular intervals. Here's an example of a ticker
that ticks periodically until we stop it. */

package main
import "time"
import "fmt"

func main() {
    ticker := time.NewTicker(time.Millisecond * 500)
    go func() {
        for t := range ticker.C {
            fmt.Println("Tick at", t)
        }
    }()
    /* Tickers use a similar mechanism to timers:
    a channel that is sent values. Here we'll use the
    `range` builtin on the channel to iterate over the
    values as they arrive every 500ms. */

    time.Sleep(time.Millisecond * 1600)
    ticker.Stop()
    fmt.Println("Ticker stopped")
    /* Tickers can be stopped like timers. Once a ticker is
    stopped it won't receive any more values on its channel.
    We'll stop ours after 1600ms. */
}
// Tick at 2017-05-01 22:20:00.499980125 +0800 CST
// Tick at 2017-05-01 22:20:00.999951087 +0800 CST
// Tick at 2017-05-01 22:20:01.499944354 +0800 CST
// Ticker stopped

// When we run this program the ticker should tick 3 times
// before we stop it.
