package main

func main() {
    data := [3]string{"a", "b", "c"}
    for i, s := range data {
        println(&i, &s)
    }
}
// 0xc420039ef0 0xc420039f08
// 0xc420039ef0 0xc420039f08
// 0xc420039ef0 0xc420039f08
