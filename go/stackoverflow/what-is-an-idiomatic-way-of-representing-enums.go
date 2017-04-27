// http://stackoverflow.com/questions/14426366/what-is-an-idiomatic-way-of-representing-enums-in-go

const ( // iota is reset to 0
    c0 = iota   // c0 == 0
    c1 = iota   // c1 == 1
    c2 = iota   // c2 == 2
)

const (
    a = 1 << iota   // a == 1 (iota has been reset)
    b = 1 << iota   // b == 2
    c = 1 << iota   // c == 4
)

const (
    u         = iota * 42   // u == 0       (untyped integer constant)
    v float64 = iota * 42   // v == 42.0    (float64 constant)
    w         = iota * 42   // w == 84      (untyped integer constant)
)

const x = iota  // x == 0 (iota has been reset)
const y = iota  // y == 0 (iota has been reset)

const (
    bit0, mask0 = 1 << iota, 1<<iota - 1    // bit0 == 1, mask0 == 0
    bit1, mask1                             // bit1 == 2, mask1 == 1
    _, _                                    // skips iota == 2
    bit3, mask3                             // bit3 == 8, mask3 == 7
)

const (
    A = iota
    C
    T
    G
)

type Base int
const (
    A Base = iota
    C
    T
    G
)
