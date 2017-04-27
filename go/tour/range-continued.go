package main
import "fmt"

func main() {
    pow := make([]int, 10)
    for i := range pow {
        pow[i] = 1 << uint(i) // == 2**i // !!!
    }
    for _, value := range pow {
        fmt.Printf("%d\n", value)
    }
}
// 1
// 2
// 4
// 8
// 16
// 32
// 64
// 128
// 256
// 512
