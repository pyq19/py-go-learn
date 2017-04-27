// http://stackoverflow.com/questions/1760757/how-to-efficiently-concatenate-strings-in-go
// 如何有效率地连接字符串

/*
In Go, string is a primitive type, it's readonly, every manipulation to it will create a new string.
So, if I want to concatenate strings many times without knowing the length of the resulting string, what's the best way to do it?
The naive way would be:

s := ""
for i := 0; i < 1000; i++ {
    s += getShortStringFromSomewhere()
}
return s

but that does not seem very efficient
*/

///////////

// The best way is to use the `bytes` package.
// It has a `Buffer` type which implements `io.Writer`

package main
import (
    "bytes"
    "fmt"
)
func main() {
    var buffer bytes.Buffer

    for i := 0; i < 1000; i++ {
        buffer.WriteString("a")
    }

    fmt.Println(buffer.String())
}
// aaaaaa.....

// This does it in O(n) time.
