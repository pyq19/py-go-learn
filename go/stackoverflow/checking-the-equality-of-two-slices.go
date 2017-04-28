// http://stackoverflow.com/questions/15311969/checking-the-equality-of-two-slices
// Checking the equality of two slices

// How can I check if two slices are equal?

///////////////////////
/*
// You need to loop over each of the elements in the slice and test.
// Equality for slices is not defined.
// However, there is a `bytes.Equal` function if you are comparing values of type `[]byte`.

func testEq(a, b []Type) bool {
    if a == nil && b == nil {
        return true
    }
    if a == nil || b == nil {
        return false
    }
    if len(a) != len(b) {
        return false
    }
    for i := range a {
        if a[i] != b[i] {
            return false
        }
    }
    return true
}
*/
/////////////////////////
/*
// You should use `reflect.DeepEqual()`.
package main
import (
    "fmt"
    "reflect"
)
func main() {
    a := []int {1, 2, 3}
    b := []int {1, 2, 3}
    c := []int {1, 2, 2}

    fmt.Println(reflect.DeepEqual(a,b))
    fmt.Println(reflect.DeepEqual(a,c))
}
// true
// false
*/
///////////////////////////
