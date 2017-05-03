package main
import "fmt"
func main() {
    var a string = "initial"
    fmt.Println(a)
    // var declares 1 or more variables

    var b, c int = 1, 2
    fmt.Println(b, c)
    // You can declare multiple variables at once.

    var d = true
    fmt.Println(d)
    // Go will infer(推断) the type of initialized variables.

    var e int
    fmt.Println(e)
    // Variables declared without a corresponding(相当的,相似,相配) initialization are `zero-valued`.
    //For example, the zero value for an `int` is 0.

    f := "short"
    fmt.Println(f)
    // The `:=` syntax is shorthand for declaring and initializing a variable,
    // e.g. for `var f string = "short"` in this case.
}
// initial
// 1 2
// true
// 0
// short
