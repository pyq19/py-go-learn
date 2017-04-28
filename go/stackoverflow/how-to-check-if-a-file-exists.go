// http://stackoverflow.com/questions/12518876/how-to-check-if-a-file-exists-in-go

// Go's standard library does not have a function solely intended to check if a file exists or not
// (like Python's `os.path.exists`).
// What is the idiomatic way to do it?

/////////////

// There isn't one, though there is no need to write a wrapper function,
// because you can directly use `os.Stat` and `os.IsNotExist` in a single line.

// To check if a file doesn't exist, equivalent to Python's
// `if not os.path.exists(filename)` :

if _, err := os.Stat("/path/to/whatever"); os.IsNotExist(err) {
    // path/to/whatever does not exist
}

// In the above example we are not checking `if err != nil` because
// `os.IsNotExist(nil) == false`.

// To check if a file exists, equivalent to Python's 
// `if os.path.exists(filename)`:

if _, err := os.Stat("/path/to/whatever"); err == nil {
    // path/to/whatever exists
}

//////////////////

// Exists reports whether the named file or directory exists.
func Exists(name string) bool {
    if _, err := os.Stat(name); err != nil {
        if os.IsNotExist(err) {
            return false
        }
    }
    return true
}
