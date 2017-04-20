// 使用有缓冲的通道和固定数目
package main
import (
    "fmt"
    "math/rand"
    "sync"
    "time"
)

const (
    numberGoroutines = 4        // 要使用的goroutine 的数量
    taskLoad         = 10       // 要处理的工作的数量
)

var wg sync.WaitGroup           // wg 同来等待程序完成

func init() {                   // init 初始化包，go 语言运行时会在其他代码执行之前优先执行这个函数
    rand.Seed(time.Now().Unix())// 初始化随机数种子
}

func main() {
    tasks := make(chan string, taskLoad)        // 创建一个有缓冲的通道来管理工作

    wg.Add(numberGoroutines)    // 启动goroutine 来处理工作
    for gr := 1; gr <= numberGoroutines; gr++ {
        go worker(tasks, gr)

    }

    for post := 1; post < taskLoad; post++ {    // 增加一组要完成的工作
        tasks <- fmt.Sprintf("task : %d", post)
    }

    close(tasks)                // 当所有工作都处理完时关闭通道，以便所有goroutine 退出

    wg.Wait()                   // 等待所有工作完成
}

func worker(tasks chan string, worker int) {    // worker 作为goroutine 启动来处理从有缓冲通道传入的工作
    defer wg.Done()

    for {
        task, ok := <-tasks     // 等待分配工作
        if !ok {
            fmt.Printf("worker: %d : shutting down\n", worker)  // 意味着通道已经空了，并且已经关闭
            return
        }

        fmt.Printf("worker: %d : started %s\n", worker, task)   // 开始工作

        sleep := rand.Int63n(100)               // 随机等待一段时间来模拟工作
        time.Sleep(time.Duration(sleep) * time.Millisecond)

        fmt.Printf("worker: %d : completed %s \n", worker, task)// 显示工作完成
    }
}

/*
worker: 2 : started task : 1
worker: 4 : started task : 4
worker: 1 : started task : 2
worker: 3 : started task : 3
worker: 1 : completed task : 2
worker: 1 : started task : 5
worker: 3 : completed task : 3
worker: 3 : started task : 6
worker: 4 : completed task : 4
worker: 4 : started task : 7
worker: 2 : completed task : 1
worker: 2 : started task : 8
worker: 1 : completed task : 5
worker: 1 : started task : 9
worker: 4 : completed task : 7
worker: 4 : shutting down
worker: 3 : completed task : 6
worker: 2 : completed task : 8
worker: 3 : shutting down
worker: 2 : shutting down
worker: 1 : completed task : 9
worker: 1 : shutting down
*/
