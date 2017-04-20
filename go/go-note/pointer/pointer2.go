package main
import "fmt"


// 实现参数+1
func add(a *int) int {
    *a = *a + 1
    return *a
}

func main() {
    x := 3
    fmt.Println("x ->", x)      // x -> 3
    x1 := add(&x)               // 传入x 的地址
    fmt.Println("x+1 = ", x1)   // x+1 =  4
    fmt.Println("x = ", x)      // x =  4
}



