// 跑不起

package main

import "C"
import "fmt"
import "unsafe"


func main() {
    s := "hello world"

    cs := C.CString(s)      //该函数在 C heap 分配内存，需要调用free释放
    defer C.free(unsafe.Pointer(cs)) // #include <stdlib.h>

    c.test(cs)
    cs = C.cstr()

    fmt.Println(C.GoString(cs))
    fmt.Println(C.GoStringN(cs, 2))
    fmt.Println(C.GoBytes(unsafe.Pointer(cs), 2))
}
