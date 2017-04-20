package main

import "time"
// import "random"


func NewTest() chan int {
    c := make(chan int)
    rand.Seed(time.Now().UnixNano())

    go func() {
        time.Sleep(time.Second)
        c <- rand.Int()
    }()

    return c
}

func main() {
    t := NewTest()
    println(<-t)        // 等待 goroutine 结束返回
}
