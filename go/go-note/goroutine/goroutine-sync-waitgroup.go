package main
import (
    "sync"
    "time"
)

func main() {
    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)               // 累加计数
        go func(id int) {
            defer wg.Done()     // 递减计数
            time.Sleep(time.Second)
            println("goroutine..", id, "done")
        }(i)
    }
    println("main...")
    wg.Wait()                   // 阻塞，直到计数归零
    println("main exit....")

}
// main...
// goroutine.. 8 done
// goroutine.. 3 done
// goroutine.. 1 done
// goroutine.. 9 done
// goroutine.. 6 done
// goroutine.. 2 done
// goroutine.. 7 done
// goroutine.. 4 done
// goroutine.. 5 done
// goroutine.. 0 done
// main exit....
