package main

func main() {
    done := make(chan struct{})
    c := make(chan int)

    go func() {
        defer close(done)

        for x := range c{   // 循环获取消息，直到通道被关闭
            println(x)
        }
    }()

    c<-1
    c<-2
    c<-3
    close(c)

    <-done
}
// 1
// 2
// 3
