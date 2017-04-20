package main

func main() {
    s := "abc"

    for i := range s {              // 忽略2nd value，支持string/array/slice/map
        println(s[i])
    }

    for _, c := range s {           // 忽略index
        println(c)
    }

    for range s {                   // 忽略全部返回值，仅迭代
//        ...
    }

    m := map[string]int{"a": 1, "b": 2}

    for k, v := range m {           // 返回{key, value}
        println(k, v)
    }
}
// 97
// 98
// 99
// 97
// 98
// 99
// a 1
// b 2
