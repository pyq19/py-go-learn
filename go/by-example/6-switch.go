// `switch` statements express conditionals across many branches.

package main
import "fmt"
import "time"
func main() {

    fmt.Println(time.Now())
    // 2017-04-30 20:35:20.601809674 +0800 CST

    i := 2
    fmt.Print("write ", i, "as ")
    switch i {
    case 1:
        fmt.Println("one")
    case 2:
        fmt.Println("two")
    case 3:
        fmt.Println("three")
    }
    // write 2as two

    switch time.Now().Weekday() {
    case time.Saturday, time.Sunday:
        fmt.Println("It's the weekend")
    default:
        fmt.Println("It's a weekday")
    }
    // It's the weekend
    // You can use commas to separate multiple expressions
    // in the same `case` statement. We use the optional `default`
    // case in the example as well.

    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("It's before noon")
    default:
        fmt.Println("It's after noon")
    }
    // It's after noon
    // `switch` without an expression is an alternate way to
    // express if/else logic. Here we also show how the case 
    // expressions can be non-constants.

    whatAmI := func(i interface{}) {
        switch t := i.(type) {
        case bool:
            fmt.Println("I'm a bool")
        case int:
            fmt.Println("I'm an int")
        default:
            fmt.Printf("Don't know type %T\n", t)
        }
    }
    whatAmI(true)
    whatAmI(1)
    whatAmI("hey")
    // I'm a bool
    // I'm an int
    // Don't know type string
    // A type `switch` compares types instead of values.
    // You can use this to discover the type of an interface value.
    // In this example, the variable `t` will have the type
    // corresponding (相当的,一致的) to its clause(条款).
}


