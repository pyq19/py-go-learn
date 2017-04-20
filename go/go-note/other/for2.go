package main

func length(s string) int {
    println("call length...")
    return len(s)
}

func main() {
    s := "abcd"

    for i, n := 0, length(s); i < n; i++ {  // 避免多次调用length 函数
        println(i, s[i])
    }
}
// call length...
// 0 97
// 1 98
// 2 99
// 3 100
