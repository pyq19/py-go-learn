package main
import "fmt"

func test(a... int) {
    fmt.Println(a)
}

func main() {
    a := [3]int{10, 20, 30}
    test(a[:]...)       // 转换为slice后展开
}
// [10 20 30]
