// http://stackoverflow.com/questions/8032170/how-to-assign-string-to-bytes-array
// How to assign string to bytes array
/*
// I want to assign string to bytes array:
var arr [20]byte
str := "abc"
for k, v := range []byte(str) {
    arr[k] = byte[v]
}
// Have another method?

//////////////////////////

// Safe and simple:
[]byte("Here is a string...")
*/
/////////////////////////
/*
package main
import "fmt"
func main() {
    s := "abc"
    var a [20]byte
    copy(a[:], s)
    fmt.Println("s:", []byte(s), "a:", a)
}
// s: [97 98 99] a: [97 98 99 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
*/
////////////////////

// Piece of cake:
// arr := []byte("That's all folks!!")

///////////

package main
import "fmt"
func main() {
    str := "abc"
    mySlice := []byte(str)
    fmt.Printf("%v -> '%s'", mySlice, mySlice)
}
// [97 98 99] -> 'abc'%
