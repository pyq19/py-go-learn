package main

func main() {
    s := "abc"

    for i, n := 0, len(s); i < n; i++ {     // 常见的for 循环，支持初始化语句
        println(s[i])
    }

    n := len(s)
    for n > 0 {                             // 替代while (n > 0) {}
        println(s[n])                       // 替代for (; n > 0;) {}
        n--
    }

    for {                                   // 替代 while (true) {}
        println(s)                          // 替代 for (;;) {}
    }
}
// 97
// 98
// 99
// panic: runtime error: index out of range
// 
// goroutine 1 [running]:
// main.main()
//     /Users/Mccree/p/py-go-learn/go/go-note/other/for_.go:12 +0xf3
//     exit status 2
