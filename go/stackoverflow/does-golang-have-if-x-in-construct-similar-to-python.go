// http://stackoverflow.com/questions/15323767/does-golang-have-if-x-in-construct-similar-to-python
// Does Golang have "if x in" construct similar to Python?

// Without iterating over the entire array how can I check if 'x' in array in Go?
// Like Python: `if 'x' in array: ...`

//////////////////////
/*
// There is no built-in operator to do it in Go.
// You need to iterate over the array. You can write your own function to do it, like this:
func stringInSlice(a string, list []string) bool {
    for _, b := range list {
        if b == a {
            return true
        }
    }
    return false
}
// If you want to be able to check for membership without iterating over the whole list,
// you need to use a map instead of an array or slice, like this:
visitedURL := map[string]bool {
    "http://www.google.com": true,
    "https://paypal.com": true,
}
if visitedURL[thisSite] {
    fmt.Println("Already been here.")
}
*/
//////////////////////////
/*
// Another solution if the list contains static values.
// eg: checking for a valid value from a list of valid values:
func IsValidCategory(category string) bool {
    switch category {
    case
        "auto",
        "news",
        "sport",
        "music":
        return true
    }
    return false
}
*/
///////////////////////
// Another option is using a map as a set.
// You use just the keys and having the value be something like a boolean
// that's always true. Then you can easily check if the map contains the key or not.
// This is useful if you need the behavior of a set,
// where if you add a value multiple times it's only int the set once.

// Here's a simple example where I add random numbers as keys to a map.
// If the same number is generated more than once it doesn't matter,
// it will only appear in the final map once.
// Then I use a simple if check to see if a key is in the map or not.

package main
import (
    "fmt"
    "math/rand"
)
func main() {
    var MAX int = 10
    m := make(map[int]bool)
    for i := 0; i <= MAX; i++ {
        m[rand.Intn(MAX)] = true
    }

    for i := 0; i <= MAX; i++ {
        if _, ok := m[i]; ok {
            fmt.Printf("%v is in map\n", i)
        } else {
            fmt.Printf("%v is not in map\n", i)
        }
    }
}
// 0 is in map
// 1 is in map
// 2 is not in map
// 3 is not in map
// 4 is in map
// 5 is in map
// 6 is in map
// 7 is in map
// 8 is in map
// 9 is in map
// 10 is not in map
