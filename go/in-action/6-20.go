// 用无缓冲的通道模拟2个goroutine 间的网球比赛
package main
import (
    "fmt"
    "math/rand"
    "sync"
    "time"
)

var wg sync.WaitGroup

func init() {
    rand.Seed(time.Now().UnixNano())
}

func main() {
    court := make(chan int)     // 创建一个无缓冲的通道
    wg.Add(2)                   // 计数加2，表示要等待两个goroutine

    go player("nadal", court)
    go player("djokovic", court)

    court <- 1  // 发球
    wg.Wait()   // 等待游戏结束
}

func player(name string, court chan int) {      // 模拟一个选手在打网球
    defer wg.Done()             //  在函数退出时调用Done 通知main 函数工作已经完成
    for {
        ball, ok := <-court     // 等待球被击打过来
        if !ok {
            fmt.Printf("player %s won\n", name) // 如果通道被关闭，就赢
            return
        }

        n := rand.Intn(100)
        if n%13 == 0 {
            fmt.Printf("player %s missed\n", name)
            close(court)        // 关闭通道，表示输了
            return
        }

        fmt.Printf("player %s hit %d\n", name, ball)
        ball++

        court <- ball           // 将球打向对手
    }
}

/*
player djokovic hit 1
player nadal hit 2
player djokovic hit 3
player nadal hit 4
player djokovic hit 5
player nadal hit 6
player djokovic hit 7
player nadal hit 8
player djokovic hit 9
player nadal hit 10
player djokovic hit 11
player nadal hit 12
player djokovic missed
player nadal won
*/
