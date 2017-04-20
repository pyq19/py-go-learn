package main
import "fmt"

// 返回a, b 中最大值
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    x := 3
    y := 4
    z := 5

    max_xy := max(x, y)
    max_xz := max(x, z)

    fmt.Printf("max(%d, %d) = %d\n", x, y, max_xy)
    fmt.Printf("max(%d, %d) = %d\n", x, z, max_xz)
    fmt.Printf("max(%d, %d) = %d\n", y, z, max(y, z))
}
// max(3, 4) = 4
// max(3, 5) = 5
// max(4, 5) = 5
