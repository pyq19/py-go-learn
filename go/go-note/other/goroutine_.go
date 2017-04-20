package main
import (
    "fmt"
    "time"
)

func task(id int) {
    for i := 0; i < 5; i++ {
        fmt.Printf("%d: %d\n", id, i)
        time.Sleep(time.Second)
    }
}

func main() {
    go task(1)      // 创建goroutine
    go task(2)

    time.Sleep(time.Second * 6)
}
// 2: 0
// 1: 0
// 1: 1
// 2: 1
// 1: 2
// 2: 2
// 2: 3
// 1: 3
// 2: 4
// 1: 4
