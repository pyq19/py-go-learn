package main

func main() {
    done := make(chan struct{})     // 结束事件
    c := make(chan string)          // 数据传输通道

    go func() {
        s := <-c
        println(s)
        close(done)                 // 关闭通道，作为结束通知
    }()

    c<-"hi!!"                       // 发送消息
    <-done                          // 阻塞，直到有数据或管道关闭
}
// hi!!
