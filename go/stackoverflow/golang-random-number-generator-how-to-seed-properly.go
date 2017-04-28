// http://stackoverflow.com/questions/12321133/golang-random-number-generator-how-to-seed-properly
// Golang random number generator how to seed properly

// I am trying to generate a random string in Go and here is the code I have written so far:
/*
package main
import (
    "bytes"
    "fmt"
    "math/rand"
    "time"
)
func main() {
    fmt.Println(randomString(10))
}
func randomString(l int) string {
    var result bytes.Buffer
    var temp string
    for i := 0; i < l; {
        if string(randInt(65, 90)) != temp {
            temp = string(randInt(65, 90))
            result.WriteString(temp)
            i++
        }
    }
    return result.String()
}
func randInt(min int, max int) int {
    rand.Seed(time.Now().UTC().UnixNano())
    return min + rand.Intn(max-min)
}
// WHJADLCNTX
*/
// My implementation is very slow. Seeding using `time` brings the same random number for a certain time,
// so the loop iterates again and again. How can I improve my code?
//////////////////////
/*
package main
import (
    "fmt"
    "math/rand"
    "time"
)
func main() {
    rand.Seed(time.Now().UTC().UnixNano())
    fmt.Println(randomString(10))
}
func randomString(l int) string {
    bytes := make([]byte, l)
    for i := 0; i < l; i++ {
        bytes[i] = byte(randInt(65, 90))
    }
    return string(bytes)
}
func randInt(min int, max int) int {
    return min + rand.Intn(max-min)
}
// GOQPOUPAEK
*/
////////////////////////
/*
package main
import (
    "fmt"
    "math/rand"
    "time"
)
func main() {
    rand.Seed( time.Now().UnixNano())
    var bytes int
    for i := 0; i < 10; i++ {
        bytes = rand.Intn(6) + 1
        fmt.Println(bytes)
    }
}
// 2
// 3
// 1
// 3
// 5
// 3
// 6
// 1
// 5
// 2
*/

// This is based off the dystroy's code but fitted for my needs.

// It's die six (rands ints 1 =< i =< 6)
func randomInt(min int, max int) int {
    var bytes int
    bytes = min + rand.Intn(max)
    return int(bytes)
}

////////////////
