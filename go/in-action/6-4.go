// goroutine 调度器在单个线程上切分时间片

package main
import (
    "fmt"
    "runtime"
    "sync"
)

var wg sync.WaitGroup

func main() {
    runtime.GOMAXPROCS(1)       // 分配一个逻辑处理器给调度器使用
    wg.Add(2)
    fmt.Println("create goroutines")
    go printPrime("A")
    go printPrime("B")

    fmt.Println("waiting to finish")
    wg.Wait()

    fmt.Println("terminating program...")
}

func printPrime(prefix string) {        // printPrime 显示5000以内的素数值
    defer wg.Done()             // 在函数退出时调用Done 来通知main 函数工作已经完成

next:
    for outer := 2; outer < 5000; outer++ {
        for inner := 2; inner < outer; inner++ {
            if outer%inner == 0 {
                continue next
            }
        }
        fmt.Printf("%s:%d\n", prefix, outer)
    }
    fmt.Println("completed ->", prefix)
}

