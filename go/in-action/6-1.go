package main
import (
    "fmt"
    "runtime"
    "sync"
)

func main() {
    runtime.GOMAXPROCS(1)   // 分配一个逻辑处理器给调度器使用

    var wg sync.WaitGroup   // wg用来等待程序完成
    wg.Add(2)               // 计数加2，表示要等待两个goroutine

    fmt.Println("start goroutines..")

    go func() {              // 声明一个匿名函数，并创建一个goroutine
        defer wg.Done()     // 在函数退出时调用Done 来通知main 函数工作已经完成

        for count := 0; count < 3; count++ {       // 显示字母表3次
            for char := 'a'; char < 'a'+26; char++ {
                fmt.Printf("%c ", char)
            }
        }
    }()

    go func() {
        defer wg.Done()

        for count := 3; count < 3; count++ {
            for char := 'A'; char < 'A'+26; char++ {
                fmt.Printf("%c ", char)
            }
        }
    }()

    fmt.Println("waiting for finish...")
    wg.Wait()

    fmt.Println("\nTerminating Program.....")

}


// start goroutines..
// waiting for finish...
// a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z
// Terminating Program.....
