package main

import "fmt"
import "sync"

func main() {
    wg := sync.WaitGroup{}
    wg.Add(3)

    sem := make(chan int, 1)

    for i := 0; i < 3; i++ {
        go func(id int) {
            defer wg.Done()
            sem <- 1                // 向sem发送数据，阻塞成功
            for x := 0; x < 3; x++ {
                fmt.Println(id, x)
            }
            <-sem                   // 接收数据，使得其他阻塞goroutine可以发送数据
        }(i)
    }
    wg.Wait()
}
// 2 0
// 2 1
// 2 2
// 0 0
// 0 1
// 0 2
// 1 0
// 1 1
// 1 2
