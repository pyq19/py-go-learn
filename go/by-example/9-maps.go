// Maps are Go's built-in associative data type (sometimes called
// hashes or dicts in other languages.

package main
import "fmt"
func main() {
    m := make(map[string]int)
    // To create an empty map, use the builtin `make`
    // make(map[key-type]val-type)

    m["k1"] = 7
    m["k2"] = 13
    // Set key/value pairs using typical `name[key] = val` syntax.

    fmt.Println("map:", m)
    // map: map[k1:7 k2:13]
    // Printing a map with e.g. `Println`
    // will show all of its key/value pairs.

    v1 := m["k1"]
    fmt.Println("v1: ", v1)
    // v1:  7
    // Get a value for a key with `name[key]`.

    fmt.Println("len:", len(m))
    // len: 2
    // The builtin `len` returns the number of key/value pairs
    // when called on a map.

    delete(m, "k2")
    fmt.Println("map:", m)
    // map: map[k1:7]
    // The builtin `delete` removes key/value pairs from a map.

    _, prs := m["k2"]
    fmt.Println("prs:", prs)
    // prs: false
    /* The optional second return value when getting a value
    from a map indicates(表明,指示,显示) if the key was present in the map.
    This can be used to disambiguate(消除) between missing keys
    and keys with zero values like 0 or "".
    Here we didn't need the value itself, so we ignored it with the 
    blank identifier `_`. */

    n := map[string]int{"foo": 1, "bar": 2}
    fmt.Println("map:", n)
    // map: map[foo:1 bar:2]
    // You can also declare and initialize a new map in the same line with
    // this syntax.
}
// Note that maps appear in the form map[k:v k:v] when printed with `fmt.Println`.
