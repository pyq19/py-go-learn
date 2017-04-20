const (
    Sunday = iota   // 0
    Monday          // 1, 通常省略后续行表达式
    Tuesday         // 2
    Wednesday       // 3
    Thursday        // 4
    Friday          // 5
    Saturday        // 6
)

const (
    _           = iota              // iota = 0
    KB  int64   = 1 << (10 * iota)  // iota = 1
    MB                              // 与 KB 表达式相同，但iota = 2
    GB
    TB
)

const (
    A, B = iota, iota << 10         // 0, 0 << 10
    C, D                            // 1, 1 << 10
)

const (
    A = iota        // 0
    B               // 1
    C = "c"         // c
    D               // c, 与上一行相同
    E = iota        // 4, 显示恢复，注意计数包含类C D两行
    F               // 5
)
