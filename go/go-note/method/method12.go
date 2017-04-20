/* 用defer定义延迟调用，无论函数是否出错，
它都确保结束前被调用 */

package main

func test (a, b int) {
    // 常用来释放资源，解除锁定，或执行一些清理操作
    defer println("dispose...")
    // 可定义多个defer，按FILO 顺序执行
    println(a/b)
}

func main() {
    test(10, 0)
}
// dispose...
// panic: runtime error: integer divide by zero
