package main
import "fmt"

func main() {
    S := "abcdefg"
    fmt.Println(S[0] == '\x61', S[1] == 'b', S[2] == 0x63) // true true true

    s := "hello, world!"
    s1 := s[:5] // [0:5)
    s2 := s[7:] // (7:]
    s3 := s[1:5]// [1:5)
    fmt.Println("s ->", s, "s1 ->", s1, "s2 ->", s2, "s3 ->", s3)
    // s -> hello, world! s1 -> hello s2 -> world! s3 -> ello

    // 单引号字符常表示Unicode Code Point，支持\uFFFF \U7FFFFFFF \xFF 格式，对应rune 类型，UCS-4
    fmt.Printf("%T\n", 'a')
    var c1, c2 rune = '\u6211', '们'
    println(c1 == '我', string(c2) == "\xe4\xbb\xac")
    // int32
    // true true

    // 要修改字符串，可先转换成[]rune 或[]byte，再转成string，这些操作都会重新分配内存并复制字节数组
    S2 := "abcd"
    bs := []byte(S2)
    bs[1] = 'B'
    println(string(bs))
    u := "电脑"
    us := []rune(u)

    us[1] = '话'
    println(string(us))
    // aBcd
    // 电话

    S3 := "abc汉字"
    for i := 0; i < len(S3); i++ {  // byte
        fmt.Printf("%c,", S3[i])
    }
    fmt.Println()
    for _, r := range S3 {          // rune
        fmt.Printf("%c,", r)
    }
    // a,b,c,æ,±,,å,­,,
    // a,b,c,汉,字,%
}
