package main
import (
    "sync"
    "time"
)

func main() {
    var wg sync.WaitGroup
    ready := make(chan struct{})

    for i := 0; i < 3; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            println(id, ": ready.")     // 运动员准备就绪
            <-ready
            println(id, ": running...")
        }(i)
    }

    time.Sleep(time.Second)
    println("Ready? GO!")

    close(ready)                        // 砰！
    wg.Wait()
}
// 0 : ready.
// 2 : ready.
// 1 : ready.
// Ready? GO!
// 0 : running...
// 1 : running...
// 2 : running...
