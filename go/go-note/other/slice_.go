package main
import "fmt"

func main() {
    x := make([] int, 0.5)  // 创建容量为5的切片 ???
    for i := 0; i < 8; i++ {
        x = append(x, i)    // 追加数据。当超出容量限制时，自动分配更大的存储空间
    }
    fmt.Println(x)
}
