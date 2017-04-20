// 用无缓冲的通道模拟4个goroutine 间的接力比赛
package main
import (
    "fmt"
    "sync"
    "time"
)

var wg sync.WaitGroup

func main() {
    baton := make(chan int)         // 创建一个无缓冲的通道
    wg.Add(1)                       // 为最后一位跑步者计数加1
    go Runner(baton)                // 第一位跑步者持有接力棒
    baton <- 1                      // 开始比赛
    wg.Wait()                       // 等待比赛结束
}

func Runner(baton chan int) {       // 模拟接力比赛中的一位跑步者
    var newRunner int
    runner := <-baton               // 等待接力棒
    fmt.Printf("runner %d running with baton\n", runner)        // 开始绕着跑道跑步

    if runner != 4 {                // 创建下一位跑步者
        newRunner = runner + 1
        fmt.Printf("running %d to the line\n", newRunner)
        go Runner(baton)
    }

    time.Sleep(100 * time.Millisecond)                          // 围绕跑道跑

    if runner == 4 {                // 判断比赛是否结束
        fmt.Printf("runner %d finished, race over...\n", runner)
        wg.Done()
        return
    }

    fmt.Printf("running %d exchange with runner %d\n", runner, newRunner) // 将接力棒交给下一个跑步者

    baton <- newRunner
}
// runner 1 running with baton
// running 2 to the line
// running 1 exchange with runner 2
// runner 2 running with baton
// running 3 to the line
// running 2 exchange with runner 3
// runner 3 running with baton
// running 4 to the line
// running 3 exchange with runner 4
// runner 4 running with baton
// runner 4 finished, race over...
