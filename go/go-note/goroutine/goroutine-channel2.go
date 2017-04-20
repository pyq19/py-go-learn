package main
import "fmt"

func main() {
    data := make(chan int, 3)           // 缓冲区可以存储3个元素
    exit := make(chan bool)

    data <- 1                           // 在缓冲区未满前，不会阻塞
    data <- 2
    data <- 3

    go func() {                         // 在缓冲区未空前，不会阻塞
        for d := range data {
            fmt.Println(d)
        }
        exit <- true
    }()

    data <- 4                           // 如果缓冲区已满，阻塞
    data <- 5
    close(data)

    <-exit
}
// 1
// 2
// 3
// 4
// 5
