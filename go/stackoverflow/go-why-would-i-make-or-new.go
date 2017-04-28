// http://stackoverflow.com/questions/9320862/go-why-would-i-make-or-new
// why would I make() or new()?

// The introduction documents dedicate many paragraphs(段落) to explaining the
// difference between new() and make(), but in practice, you can create objects within local scope
// and return them.
// Why would you use the (frankly silly) pair of allocators?

//////////////////

// Things you can do with `make` that you can't do any other way:
// 1. Create a channel
// 2. Create a map with space preallocated
// 3. Create a slice with space preallocated or with len != cap

// It's a little harder to justify `new`.
// The main thing it makes easier is creating pointers to non-composite types.
// The two functions below are equivalent.
// One's just a little more concise.

func newInt1() *int { return new(int) }

func newInt2() *int {
    var i int
    return &i
}
////////////////////////

// Go has multiple ways of memory allocation(分配) and value initialization(初始化):

// &T{...}, &someLocalVar, new, make

// Allocation can also happen when creating composite(复合的，合成的) literals.

// `new` can be used to allocate values such as integers, `&int` is illegal:

new(Point)
&Point{}        // OK
&Point{2, 3}    // Combines(联合，使结合) allocation and initialization 

new(int)
&int            // Illegal

// Works, but it is less convenient to write than new(int)
var i int
&i

// The difference between `new` and `make` can be seen by looking at the following example:

p := new(chan int)      // p has type: *chan int
c := make(chan int)     // c has type: chan int

// Suppose Go does not have `new` and `make`, but it has the built-in function `NEW`.
// Then the example code would look like this:

p := NEW(*chan int)     // * is mandatory(强制的；托管的；命令的 n. 受托者（等于mandatary）)
c := NEW(chan int)

// The `*` would be `mandatory`, so:

new(int)        -> NEW(*int)
new(Point)      -> NEW(*Point)
new(chan int)   -> NEW(*chan int)
make([]int, 10) -> NEW([]int, 10)

new(Point)  // Illegal
new(int)    // Illegal

// Yes, merging `new` and `make` into a single built-in function is possible.
// However, it is probable that a single built-in function would lead to more confusion
// among new Go programmers than having two built-in functions.

// Considering all of the above points, it appears more appropriate for `new` and `make` to remain sepatate.

///////////////////////

// make function allocates and initializes an object of type slice, map or chan only.
// Like new, the first argument is a type. But it can also take a second argument, the size.
// Unlike new, make's return type is the same as the type of its argument, not a pointer to it.
// And the allocated value is initialized (not set to zero value like in new).
// The reason is that slice, map and chan are data structures.
// They need to be initialized, otherwise(否则) they won't be usable.
// This is the reason new() and make() need to be different.

// The following examples from Effective Go make it very clear:

p *[]int = new([]int)       // *p = nil, which makes p useless
v []int = make([]int, 100)  // creates v structure that has pointer to an array,
                            // length field, and capacity field.
                            // So, v is immediately(立即) usable.
