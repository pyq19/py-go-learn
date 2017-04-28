// http://stackoverflow.com/questions/1841443/iterating-over-all-the-keys-of-a-golang-map

// Is there a way to get a list of all the keys in a Go language map?
// The number of elements is given by `len()`, but if I have a map like:

// m := map[string]string{"key1": "val1", "key2": "val2"}

// how do I iterate over all the keys?

///////////////
/*
for k, v := range m {
    fmt.Printf("key[%s] value[%s]\n", k, v)
}

for k := range m {
    fmt.Printf("key[%s] value[%s]\n", k, m[k])
}
*/
/////////////

// Return keys of the given map
package main
import "fmt"
func Keys(m map[string]interface{}) (keys []string) {
    for k := range m {
        keys = append(keys, k)
    }
    return keys
}

// use `Keys` func
func main() {
    m := map[string]interface{}{
        "foo": 1,
        "bar": true,
        "baz": "baz",
    }
    fmt.Println(Keys(m))    // [foo bar baz]
}
//////////////
// ks := reflect.ValueOf(m).MapKeys()   // get a list of all the keys in a map
