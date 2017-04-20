package main
import "fmt"

type testInt func(int) bool     // 声明函数类型

func isOdd(integer int) bool {
    if integer%2 == 0 {
        return false
    }
    return true
}

func isEven(integer int) bool {
    if integer%2 == 0 {
        return true
    }
    return false
}

// 声明的函数类型在这个地方当作参数
func filter(slice []int, f testInt) []int {
    var result []int
    for _, value := range slice {
        if f(value) {
            result = append(result, value)
        }
    }
    return result
}

func main() {
    slice := []int {1, 2, 3, 4, 5, 7}
    fmt.Println("slice -> ", slice)
    odd := filter(slice, isOdd)     // 函数当做值传递
    fmt.Println("odd element of slice are -> ", odd)
    even := filter(slice, isEven)
    fmt.Println("even element of slice are -> ", even)
}
// slice ->  [1 2 3 4 5 7]
// odd element of slice are ->  [1 3 5 7]
// even element of slice are ->  [2 4]
