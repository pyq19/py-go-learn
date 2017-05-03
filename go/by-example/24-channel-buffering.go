/* By default channels are unbuffered, meaning that
they will only accept sends (chan <-) if there is a
corresponding receive (<- chan) ready to receive the sent
value. Buffered channels accept a limited number of values 
without a corresponding receiver for those values. */

package main
import "fmt"

func main() {
    messages := make(chan string, 2)
    // Here we `make` a channel of strings buffering up to 2 values.

    messages <- "buffered"
    messages <- "channel"
    // Because this channel is buffered, we can send these values
    // into the channel without a corresponding concurrent receive.

    fmt.Println(<-messages)// buffered
    fmt.Println(<-messages)// channel
    // Later we can receive these two values as usual.
}


