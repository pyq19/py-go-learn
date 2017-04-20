// 支持在函数内goto 跳转，标签名区分大小写，未使用标签引发错误

package main

/*
func main() {
    var i int
    for {
        println(i)
        i++
        if i > 2 { goto BREAK }
    }

BREAK:
    println("break..")
// EXIT:                           // Error: label EXIT defined and not uses
}
// 0
// 1
// 2
// break..
*/

func main() {
L1:
    for x := 0; x < 3; x++ {
L2:
        for y := 0; y < 5; y++ {
            if y > 2 { continue L2 }
            if x > 1 { break L1 }

            print(x, ":", y, " ")
        }
        println()
    }
}
// 0:0 0:1 0:2
// 1:0 1:1 1:2

// break 可用于for switch select，而continue 仅能用于for 循环
