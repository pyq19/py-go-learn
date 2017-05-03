// Rate limiting is an important mechanism for controlling resource
// utilization and maintaining quality of service. Go elegantly
// supports rate limiting with goroutines, channels, and tickers.

package main
import "fmt"
import "time"

func main() {
    requests := make(chan int, 5)
    for i := 1; i <= 5; i++ {
        requests <- i
    }
    close(requests)
    /* First we'll look at basic rete limiting. Suppose
    we want to limit our handling of incoming requests.
    We'll serve these requests off a channel of the same name. */

    limiter := time.Tick(time.Millisecond * 200)
    // This `limiter` channel will receive a value every 200 milliseconds.
    // This is the regulator in our rate limiting scheme.

    for req := range requests {
        <-limiter
        fmt.Println("request", req, time.Now())
    }
    // By blocking on a receive from the `limiter` channel before
    // serving each request, we limit ourselves to 1 request every 200
    // milliseconds.

    burstyLimiter := make(chan time.Time, 3)
    /* We may want to allow short bursts of requests in our rate
    limiting scheme while preserving the overall rate limit. We
    can accomplish this by buffering our limiter channel. This
    `burstyLimiter` channel will allow bursts of up to 3 events. */

    for i := 0; i < 3; i++ {
        burstyLimiter <- time.Now()
    }
    // Fill up the channel to represent allowed bursting.

    go func() {
        for t := range time.Tick(time.Millisecond * 200) {
            burstyLimiter <- t
        }
    }()
    // Every 200 milliseconds we'll try to add a new value to 
    // `burstyLimiter`, up to its limit of 3.

    burstyRequests := make(chan int, 5)
    for i := 1; i <= 5; i++ {
        burstyRequests <- i
    }
    close(burstyRequests)
    for req := range burstyRequests {
        <-burstyLimiter
        fmt.Println("request", req, time.Now())
    }
    // Now simulate 5 more incoming requests. The first 3 of these
    // will benefit from the burst capability of `burstyLimiter`.
}
// request 1 2017-05-02 21:21:05.593265849 +0800 CST
// request 2 2017-05-02 21:21:05.795863648 +0800 CST
// request 3 2017-05-02 21:21:05.995697122 +0800 CST
// request 4 2017-05-02 21:21:06.191608341 +0800 CST
// request 5 2017-05-02 21:21:06.394571596 +0800 CST
/* Running our program we see the first batch of requests
handled once every ~200 milliseconds as desired. */

// request 1 2017-05-02 21:21:06.39466783 +0800 CST
// request 2 2017-05-02 21:21:06.394681771 +0800 CST
// request 3 2017-05-02 21:21:06.394690713 +0800 CST
// request 4 2017-05-02 21:21:06.595823163 +0800 CST
// request 5 2017-05-02 21:21:06.795708391 +0800 CST
/* For the second batch of requests we serve the first 3
immediately because of the burstable rate limiting, then
serve the remaining 2 with ~200ms delays each. */
