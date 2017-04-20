package main
import "fmt"


func test(a... int) {
    for i := range a{
        a[i] += 100
    }
}

func main() {
    a := []int {10, 20, 30}
    test(a...)

    fmt.Println(a)
}
// [110 120 130]
