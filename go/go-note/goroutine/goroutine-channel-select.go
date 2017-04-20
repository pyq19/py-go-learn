package main

import "fmt"
import "os"

func main() {
    a, b := make(chan int, 3), make(chan int)

    go func() {
        v, ok, s := 0, false, ""

        for {
            select {                            // 随机选择可用 channel，接收数据
            case v, ok = <-a: s = "a"
            case v, ok = <-b: s = "b"
            }

            if ok {
                fmt.Println(s, v)
            } else {
                os.Exit(0)
            }
        }
    }()

    for i := 0; i < 5; i++ {
        select {                                // 随机选择可用channel，发送数据
        case a <- i:
        case b <- i:
        }
    }

    close(a)
    select {}                                   // 没有可用channel，阻塞main goroutine
}
// b 3
// b 4
// a 0
// a 1
// a 2
