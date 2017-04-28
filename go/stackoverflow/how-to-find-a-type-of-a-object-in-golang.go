// http://stackoverflow.com/questions/20170275/how-to-find-a-type-of-a-object-in-golang
// How to find a type of a object in Golang?

////////////////////////
/*
// The Go reflection(反射) package has methods for inspecting the type of variables.
// The following snippet will print out the reflection type of a string, integer and float.

package main
import (
    "fmt"
    "reflect"
)
func main() {
    tst := "string"
    tst2 := 10
    tst3 := 1.2

    fmt.Println(reflect.TypeOf(tst))
    fmt.Println(reflect.TypeOf(tst2))
    fmt.Println(reflect.TypeOf(tst3))
}
// string
// int
// float64
*/
/////////////////////////
/*
// I found 3 ways to recognize type at runtime:

// 1. Using `string formatting`
func typeof(v interface{}) string {
    return fmt.Sprintf("%T", v)
}

// 2. Using `reflect package`
func typeof(v interface{}) string {
    return reflect.TypeOf(v).String()
}

// 3. Using `type assertions`
func typeof(v interface{}) string {
    switch t := v.(type) {
    case int:
        return "int"
    case float64:
        return "float64"
    // ... etc
    default:
        _ = t
        return "unknown"
    }
}
*/
/////////////////////////////////

package main
import (
    "fmt"
    "reflect"
)
func main() {
    b := true
    s := ""
    n := 1
    f := 1.0
    a := []string{"foo", "bar", "baz"}

    fmt.Println(reflect.TypeOf(b))
    fmt.Println(reflect.TypeOf(s))
    fmt.Println(reflect.TypeOf(n))
    fmt.Println(reflect.TypeOf(f))
    fmt.Println(reflect.TypeOf(a))
}
// bool
// string
// int
// float64
// []string
