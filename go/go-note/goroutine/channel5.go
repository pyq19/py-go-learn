package main

func main() {
    c := make(chan int, 3)

    c<-10
    c<-20
    close(c)

    for i := 0; i < cap(c) + 1; i++ {
        x, ok := <-c
        println(i, ":", ok, x)
    }
}
// 0 : true 10
// 1 : true 20
// 2 : false 0
// 3 : false 0
