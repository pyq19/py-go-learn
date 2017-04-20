package main
import "fmt"

/*
a := [3]int{1, 2}           // 未初始化元素值为 0
b := [...]int{1, 2, 3, 4}   // 通过初始化值确定数组长度
c := [5]int{2: 100, 4:200}  // 使用索引号初始化元素

d := [...]struct {
    name string
    age uint8
}{
    {"user1", 10},          // 可省略元素类型
    {"user2", 20},          // 注意最后一行逗号
}

// 多维数组
a := [2][3]int{{1, 2, 3}, {4, 5, 6}}
b := [...][2]int{{1, 1}, {2, 2}, {3, 3}}    // 第2纬度不能用"..."
*/

func test(x [2]int) {
    fmt.Printf("x: %p\n", &x)
    x[1] = 1000
}

func main() {
    a := [2]int{}
    fmt.Printf("a -> %p\n", &a)
    test(a)
    fmt.Println(a)
}

// a -> 0xc42000e250
// x: 0xc42000e270
// [0 0]
