// http://stackoverflow.com/questions/21362950/golang-getting-a-slice-of-keys-from-a-map
// Getting a slice of keys from a map

// Is there any simpler/nicer way of getting a slice of keys from a map in Go?
// Currently I am iterating over the map and copying the keys to a slice
/*
i := 0
keys := make([]int, len(mymap))
for k := range mymap {
    keys[i] = k
    i++
}
*/
/////////////////////
/*
package main
func main() {
    mymap := make(map[int]string)
    keys := make([]int, 0, len(mymap))
    for k := range mymap {
        keys = append(keys, k)
    }
}
// To be efficient in Go, it's important to minimize memory allocations.
*/
/////////////////

// You also can take an array of keys with type `[]Value` by method `MapKeys` of struct `Value` from package "reflect":
package main
import (
    "fmt"
    "reflect"
)
func main() {
    abc := map[string]int{
        "a": 1,
        "b": 2,
        "c": 3,
    }
    keys := reflect.ValueOf(abc).MapKeys()

    fmt.Println(keys)
}
// [a b c]
