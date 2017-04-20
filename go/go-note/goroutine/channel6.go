package main
import "time"

func main() {
    exit := make(chan struct{})     // 创建通道，因为仅是通知，数据并没有实际意义
    go func() {
        time.Sleep(time.Second)
        println("goroutine done...")

        close(exit)                 // 关闭通道，发出信号
    }()

    println("main....")
    <-exit                          // 如通道关闭，立即解除阻塞

    println("main exit.....")
}
// main....
// goroutine done...
// main exit.....
