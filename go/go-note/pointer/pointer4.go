package main

func main() {
    a := struct {
        x int
    }{}

    a.x = 100
    p := &a
    p.x += 100      // 相当于p->x += 100

    println(p.x)
    println(p)
    println(&p)
//    println(*p)   // ERROR !!
}
// 200
// 0xc420039f68
// 0xc420039f70
