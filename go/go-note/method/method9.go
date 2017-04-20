package main
import "fmt"

// 变参 本质上是slice

func test(s string, n ...int) string {
    var x int
    for _, i := range n {
        x += i
    }

    return fmt.Sprintf(s, x)
}

/*
func main() {
    println(test("sum -> %d", 1, 2, 3))
}
// sum -> 6
*/

// 使用slice 对象做变参时，必须展开
func main() {
    s := []int{1, 2, 3}
    println(test("sum -> %d", s...))
}
// sum -> 6
