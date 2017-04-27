// http://stackoverflow.com/questions/2050391/how-to-check-if-a-map-contains-a-key-in-go

// I know I can iterate over a map m by:
// for k, v := range m { ... }

// and look for a key but is there a more efficient way of testing a key's existence in a map?

///////////
/*
if val, ok := dict["foo"]; ok {
    // do something here
}
*/
/////////
package main
import "fmt"
func main() {
    dict := map[string]int {"foo" : 1, "bar" : 2}
    value, ok := dict["baz"]
    if ok {
        fmt.Println("value ->", value)
    } else {
        fmt.Println("key not found ..") // key not found ..
    }
}
// Or, more compactly(简洁地)
/*
if value, ok := dict["baz"]; ok {
    fmt.Println("value ->", value)
} else {
    fmt.Println("key not found")
}
*/
