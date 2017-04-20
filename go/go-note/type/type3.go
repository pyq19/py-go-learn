package main
// import "fmt"

type Color int

const (
    Black Color = iota
    Red
    Blue
)

func test(c Color) {}

func main() {
    c := Black
    test(c)

//    x := 1
//    test(x) // Error: cannot use x (type int) as type Color in function argument
    test(1) // 常量会被编译器自动转化
}
// ./type3.go:19: cannot use x (type int) as type Color in argument to test
