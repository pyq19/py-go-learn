package main
import (
    "time"
)


var c int

func counter() int{
    c++
    return c
}

func main() {
    a := 100
    go func(x, y int) {
        time.Sleep(time.Second)     // 让goroutine在main逻辑之后执行
        println("go:", x, y)
    }(a, counter())                 // 立即计算并复制参数

    a += 100
    println("main:", a, counter())

    time.Sleep(time.Second * 3)         // 等待goroutine结束
}
// main: 200 2
// go: 100 1
