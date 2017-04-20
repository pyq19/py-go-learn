// 如果存在多个channel，通过select 可以监听channel 上的数据流动
// select 默认是阻塞的，只有监听的channel 中发送或接受可以进行时才会运行
// 当多个channel 都准备好时，select 随机选择一个执行
// 不明白

package main
import "fmt"

func fibonacci(c, quit chan int) {
    x, y :=  1, 1
    for {
        select {
        case c <- x:
            x, y = y, x + y
        case <-quit:
            fmt.Println("quit")
            return
        }
    }
}

func main() {
    c := make(chan int)
    quit := make(chan int)
    go func() {
        for i := 0; i < 10; i++ {
            fmt.Println(<-c)
        }
        quit <- 0
    }()
    fibonacci(c, quit)
}
// 1
// 1
// 2
// 3
// 5
// 8
// 13
// 21
// 34
// 55
// quit
