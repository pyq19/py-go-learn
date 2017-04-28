// http://stackoverflow.com/questions/12655464/can-functions-be-passed-as-parameters-in-go
// Can Functions be passed as parameters in Go?

// In Java I can do something like `derp(new Runnable {public void run () {/* run this sometime later */}})
// and "run" the code in the method later.
// It's a pain to handle (anonymous inner class), but it can be done.
// Does Go have something that can facilitate(促进，帮助，使容易) a 
// function/callback being passed in as a parameter?

////////////////////////////
/*
package main
import "fmt"

// convert types take an int and return a string value.
type convert func(int) string

// value implements convert, returning x as string.
func value(x int) string {
    return fmt.Sprintf("%v", x)
}

// quote123 passes 123 to convert func and returns quoted string.
func quote123(fn convert) string {
    return fmt.Sprintf("%q", fn(123))
}

func main() {
    var result string
    result = value(123)
    fmt.Println(result)

    result = quote123(value)
    fmt.Println(result)

    result = quote123(func(x int) string {return fmt.Sprintf("%b", x) })
    fmt.Println(result)

    foo := func(x int) string {return "foo"}
    result = quote123(foo)
    fmt.Println(result)

    _ = convert(foo)
}
// 123
// "123"
// "1111011"
// "foo"
*/
////////////////////////
/*
// You can pass function as parameter to a Go function.
// Here is an example of passing function as parameter to another Go function:

package main
import "fmt"

type fn func(int)

func myfn1(i int) {
    fmt.Printf("\ni is %v", i)
}
func myfn2(i int) {
    fmt.Printf("\ni is %v", i)
}
func test(f fn, val int) {
    f(val)
}
func main() {
    test(myfn1, 123)
    test(myfn2, 321)
}
// i is 123
// i is 321%
*/
//////////////////////
/*
package main
import "fmt"

func plusTwo() (func(v int) (int)) {
    return func(v int) (int) {
        return v + 2
    }
}

func plusX(x int) (func(v int) (int)) {
    return func(v int) (int) {
        return v + x
    }
}

func main() {
    p := plusTwo()
    fmt.Printf("3+2: %d\n", p(3))

    px := plusX(3)
    fmt.Printf("3+3: %d\n", px(3))
}
// 3+2: 5
// 3+3: 6
*/
