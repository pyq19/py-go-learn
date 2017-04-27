package main
import "fmt"

func main() {
    var i interface{} = "hello"

    s := i.(string)
    fmt.Println(s)

    s, ok := i.(string)
    fmt.Println(s, ok)

    f, ok := i.(float64)
    fmt.Println(f, ok)

    f = i.(float64)     // panic
    fmt.Println(f)
}
// hello
// hello true
// 0 false
// panic: interface conversion: interface {} is string, not float64
// 
// goroutine 1 [running]:
// main.main()
//     /Users/Mccree/p/py-go-learn/go/tour/type-assertions.go:16 +0x371
//     exit status 2
