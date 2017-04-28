// i := 123
// s := string(i)

// s is 'E', but what I want is "123"
// Please tell me how can I get "123".
// And in Java, I can do in this way:
// String s = "ab" + "c" // s is "abc"
// how can I concat two strings in Go?

///////////

// Use the `strconv` package's `Itoa` function.

package main
import (
    "strconv"
    "fmt"
)
func main() {
    t := strconv.Itoa(123)
    fmt.Println(t) // 123
}

// You can concat strings simply by `+` ing them, or by using the `join` function of `strings` package.

//////////////

// fmt.Sprintf("%v", value)
// If you know the specific type of value use the corresponding formatter for example `%d` for `int`
