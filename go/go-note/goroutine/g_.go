package main
import (
    "fmt"
    "runtime"
)

func say(s string) {
    for i := 0; i < 5; i++ {
        runtime.Gosched()       // 表示让CPU 把时间片让给别人，下次某个时候继续恢复执行该goroutine
        fmt.Println(s)
    }
}

func main() {
    go say("world")
    say("hello")
}
// hello
// world
// hello
// hello
// hello
// world
// hello
// world
// world
// world
